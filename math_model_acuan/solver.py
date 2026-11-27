"""Solve a profile and build its cost–emissions sample with ε-constraint."""
from pathlib import Path
from random import Random
import numpy as np
from scipy.sparse import coo_matrix, csr_matrix, hstack, vstack
from inti_solver import Bounds, LinearConstraint, PROFILES, FEAS, GAP, SolverWork, network, one_thread_milp

SOURCE = Path(__file__).resolve().parents[1] / "case/Data_Bersama.json"
PAKET_FINAL = (*range(10101, 10111), *range(10301, 10311))
JUMLAH_BATAS = 25

def buat_paket(template, seed):
    """Variasi tarif dan permintaan dengan jumlah ton per produk tetap."""
    import copy
    data = copy.deepcopy(template)
    trials = Random(seed*1009+1)
    data["biaya_buka_gudang"] = [round(x*trials.uniform(.95,1.05),3)
                              for x in data["biaya_buka_gudang"]]
    for key in ("tarif_masuk_per_ton","tarif_keluar_per_ton"):
        data[key] = [[round(x*trials.uniform(.97,1.03),3) for x in row] for row in data[key]]
    demand = template["level"]["L"]["permintaan_dasar"].copy()
    for p in "ABC":
        keys = [k for k in demand if k.endswith(","+p)]
        changes = [trials.uniform(-.20,.20) for _ in keys]
        avg = sum(changes)/len(changes)
        for key, offset in zip(keys,changes):
            demand[key] += offset-avg
    return data, demand

def assemble(data, demand, level, stochastic):
    spec = data["level"][level]
    net = network(data, spec["jalur_masuk"], spec["jalur_keluar"], demand, stochastic)
    positions = [(row, idx) for row, scenario, warehouse in net.time_rows
                 for idx,(s,g,_) in enumerate(net.groups) if (s,g)==(scenario,warehouse)]
    return csr_matrix(net.linear),net.lower,net.upper,net.bounds,net.cost,net.emission,csr_matrix(net.aggregation),net.weights,np.arange(4),positions

class CheckedMILP:
    def __init__(self, solver):
        self.solver = solver
        self.calls = self.nodes = self.retries = 0

    def __call__(self, *args, **kwargs):
        def call():
            result = self.solver(*args, **kwargs)
            self.calls += 1
            self.nodes += int(result.mip_node_count or 0)
            return result

        def inconsistent(result):
            return result.success and abs(result.fun - result.mip_dual_bound) > 5e-8

        result = call()
        if inconsistent(result):
            self.retries += 1
            kwargs['options'] = {**kwargs['options'], 'presolve': False}
            result = call()
            if inconsistent(result):
                raise RuntimeError('Penyelesaian ulang masih memberi batas objektif yang berbeda.')
        return result

class ParetoMILP(CheckedMILP):
    def __call__(self, *args, **kwargs):
        try:
            return super().__call__(*args, **kwargs)
        except RuntimeError as err:
            if str(err) != 'Penyelesaian ulang masih memberi batas objektif yang berbeda.':
                raise
        self.retries += 1
        self.calls += 1
        options = {**kwargs['options'], 'presolve':False, 'mip_feasibility_tolerance':1e-8}
        result = self.solver(*args, **{**kwargs, 'options':options})
        self.nodes += int(result.mip_node_count or 0)
        return result

class EpsilonModel:
    def __init__(self, data, model, nonlinear, solver):
        self.original, self.lower, self.upper, ub, self.cost, self.emission, self.volume, self.probability, binary, handling = model
        self.n = self.original.shape[1]
        self.k = len(self.probability) if nonlinear else 0
        self.solver = solver
        self.gap = GAP if nonlinear else 1e-7
        config = data['kontrol_profil']
        self.alpha = config['kenaikan_biaya_kuadratik'] if nonlinear else 0.
        beta = config['kenaikan_waktu_kuadratik'] if nonlinear else 0.
        rows, cols = zip(*handling) if nonlinear else ((), ())
        self.enrich = csr_matrix((np.full(len(rows), beta), (rows, cols)), shape=(len(self.upper), self.k))
        self.system = hstack([self.original,self.enrich],format='csr')
        self.integrality = np.zeros(self.n + self.k)
        self.integrality[binary] = 1
        self.binary = binary
        self.ub = ub
        self.bounds = Bounds(np.zeros(self.n + self.k), np.r_[ub, np.full(self.k,np.inf)])
        self.cost_aug = np.r_[self.cost, self.alpha*self.probability[:self.k]]
        self.emission_aug = np.r_[self.emission, np.zeros(self.k)]
        self.pivots = [{0.,4.,8.,12.,16.,20.} for _ in range(self.k)]

    def solve(self, goal, emission_limit=np.inf, cost_limit=np.inf):
        target = self.cost_aug if goal=='C' else self.emission_aug
        lo, hi = self.lower, self.upper
        matrices = [self.system]
        extra = []
        limits = []
        for coef, limit in ((self.emission_aug,emission_limit),(self.cost_aug,cost_limit)):
            if np.isfinite(limit):
                extra.append(coef)
                limits.append(limit)
        if extra:
            matrices.append(csr_matrix(extra))
            lo = np.r_[lo,np.full(len(extra),-np.inf)]
            hi = np.r_[hi,limits]
        options = {"mip_rel_gap": 0., "time_limit": 45.}
        for _ in range(120):
            current = matrices
            below, above = lo, hi
            if self.k:
                idx = np.repeat(np.arange(self.k),[len(a) for a in self.pivots])
                t = np.array([x for v in self.pivots for x in sorted(v)])
                negative_identity = coo_matrix((-np.ones(len(t)), (np.arange(len(t)),idx)),shape=(len(t),self.k))
                cuts = hstack([self.volume[idx].multiply(2*t[:,None]),negative_identity],format='csr')
                current = [*matrices,cuts]
                below,above = np.r_[lo,np.full(len(t),-np.inf)],np.r_[hi,t*t]
            sol = self.solver(target,integrality=self.integrality,bounds=self.bounds,
                       constraints=LinearConstraint(vstack(current,format='csr'),below,above),
                       options=options)
            if not sol.success:
                raise RuntimeError(f'{goal} lim E={emission_limit:.9f} lim C={cost_limit:.9f}: {sol.message}')
            x = sol.x[:self.n]
            q = self.volume@x
            sq = q*q
            c = float(self.cost@x + self.alpha*(self.probability@sq))
            e = float(self.emission@x)
            actual = self.original@x + (self.enrich@sq if self.k else 0.)
            value = c if goal=='C' else e
            gap = value-sol.mip_dual_bound
            if (
                np.all(actual>=self.lower-FEAS) and np.all(actual<=self.upper+FEAS)
                and np.all(x>=-FEAS) and np.all(x<=self.ub+FEAS)
                and np.allclose(x[self.binary],np.rint(x[self.binary]),atol=FEAS,rtol=0)
                and e<=emission_limit+FEAS and c<=cost_limit+FEAS
                and -FEAS<=gap<=self.gap
            ):
                return dict(cost=c,emission=e,gap=float(gap),warehouses=[int(i+1) for i in np.flatnonzero(x[:4]>.5)])
            added=False
            for i in np.flatnonzero(sq[:self.k]-sol.x[self.n:]>1e-10):
                v=round(float(q[i]),11)
                if v not in self.pivots[i]:
                    self.pivots[i].add(v)
                    added=True
            if not added and 'mip_feasibility_tolerance' not in options:
                options = {**options, 'mip_feasibility_tolerance':1e-8, 'presolve':False}
                self.solver.retries += 1
                continue
            if not added:
                raise RuntimeError(f'{goal} tidak terverifikasi, gap={gap:.9g}, kelebihan biaya={c-cost_limit:.9g}, kelebihan emisi={e-emission_limit:.9g}')
        raise RuntimeError('Batas jumlah iterasi tercapai.')

def pareto(data,model,nonlinear,solver):
    m=EpsilonModel(data,model,nonlinear,solver)
    minc=m.solve('C')
    left=m.solve('E')
    # Tie-break each endpoint to retain an efficient endpoint within the stated tolerance.
    lo=m.solve('C',emission_limit=left['emission']+m.gap)
    hi=m.solve('E',cost_limit=minc['cost']+m.gap)
    limits=np.linspace(lo['emission'],hi['emission'],JUMLAH_BATAS)
    points=[{**lo,'epsilon':float(limits[0])}]
    for v in limits[1:-1]:
        c=m.solve('C',emission_limit=v)
        e=m.solve('E',emission_limit=v,cost_limit=c['cost']+m.gap)
        points.append({**e,'epsilon':float(v)})
    points.append({**hi,'epsilon':float(limits[-1])})
    tol=2*m.gap+FEAS
    unique=[]
    for p in points:
        if not any(abs(p['cost']-q['cost'])<=tol and abs(p['emission']-q['emission'])<=tol for q in unique):
            unique.append(p)
    frontier=[p for p in unique if not any(
          q['cost']<=p['cost']+tol and q['emission']<=p['emission']+tol
          and (q['cost']<p['cost']-tol or q['emission']<p['emission']-tol) for q in unique)]
    assert len(points)==JUMLAH_BATAS and all(p['emission']<=p['epsilon']+FEAS for p in points)
    return points,frontier


def jalankan(data, model, profile, solver):
    """Return all evaluated points and the distinct reported points."""
    _,multi,nonlinear=PROFILES[profile]
    if multi:
        return pareto(data,model,nonlinear,solver)
    solution=EpsilonModel(data,model,nonlinear,solver).solve('C')
    return [solution],[solution]
