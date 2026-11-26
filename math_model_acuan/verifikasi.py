"""Verifikasi formulasi acuan P1–P8 dengan Python 3, NumPy, dan SciPy."""
from argparse import ArgumentParser
from csv import DictWriter
from dataclasses import dataclass
from itertools import combinations, product
from pathlib import Path
from time import perf_counter
import json
import platform

import numpy as np
import scipy
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import csr_matrix

PROFILES = {
    "P1": (False, False, False), "P2": (True, False, False),
    "P3": (False, True, False), "P4": (True, True, False),
    "P5": (False, False, True), "P6": (True, False, True),
    "P7": (False, True, True), "P8": (True, True, True),
}
PATTERNS = list(product((0, 1), repeat=4))
GAP = 0.00025
FEAS = 0.0000002
TIE = 0.0006


class Infeasible(Exception):
    """A certified relaxation of the model is infeasible."""


@dataclass
class Network:
    linear: np.ndarray
    lower: np.ndarray
    upper: np.ndarray
    bounds: np.ndarray
    cost: np.ndarray
    emission: np.ndarray
    aggregation: np.ndarray
    time_rows: list
    names: list
    groups: list
    weights: np.ndarray


def network(data, inbound, outbound, mean, stochastic):
    probabilities = np.array([s["peluang"] for s in data["P2"]["skenario"]])
    categories = sorted({(g,p) for _,g,p in data["level"]["H"]["jalur_masuk"]})
    orders = list(product(range(1, 7), "ABC"))
    demands = [dict(mean) for _ in probabilities]
    if stochastic:
        target = data["P2"]["sasaran_permintaan"]
        for d, s in zip(demands, data["P2"]["skenario"]):
            d[target] += data["P2"]["simpangan_baku"] * s["deviasi_baku"]
    n_flows = len(inbound) + len(outbound)
    n = 4 + 3*n_flows
    m = 130
    matrix = np.zeros((m, n))
    lower = np.full(m, -np.inf)
    upper = np.zeros(m)
    bounds = np.r_[np.ones(4), np.full(n-4, np.inf)]
    energy = np.r_[data["P3"]["emisi_tetap_gudang"], np.zeros(n-4)]
    cost = np.r_[data["biaya_buka_gudang"], np.zeros(n-4)]
    names = [f"y[{g}]" for g in range(1,5)]
    settings = data["kontrol_profil"]
    groups = {}
    time_rows = []
    for s, (demand, probability) in enumerate(zip(demands, probabilities)):
        offset = s*39
        i0 = 4+s*n_flows
        upper[offset:offset+6] = data["kapasitas_pabrik"]
        upper[offset+17:offset+35] = [demand.get(f"{j},{p}", 0) for j,p in orders]
        lower[offset+6:offset+35] = upper[offset+6:offset+35]
        for k, (i,g,p) in enumerate(inbound, i0):
            matrix[offset+i-1,k] = 1
            matrix[offset+6+categories.index((g,p)),k] = 1
            cost[k] = probability * data["tarif_masuk_per_palet"][i-1][g-1]
            energy[k] = probability * data["P3"]["emisi_masuk_per_palet"][i-1][g-1]
            names.append(f"x[{i},{g},{p},{s+1}]")
        for k, (g,j,p) in enumerate(outbound, i0+len(inbound)):
            matrix[offset+6+categories.index((g,p)),k] = -1
            matrix[offset+17+orders.index((j,p)),k] = 1
            matrix[offset+34+g,k] = 1
            cost[k] = probability * (data["tarif_keluar_per_palet"][g-1][j-1]
                                      + data["tarif_penanganan_per_palet"][g-1]["ABC".index(p)])
            energy[k] = probability * data["P3"]["emisi_keluar_per_palet"][g-1][j-1]
            names.append(f"z[{g},{j},{p},{s+1}]")
            groups.setdefault((s,g,p), []).append(k)
        for g in range(1,5):
            capacity = offset+34+g
            time = 118+4*s+g-1
            matrix[time] = matrix[capacity] * settings["waktu_per_palet"]
            matrix[time,g-1] = -settings["waktu_gudang"][g-1]
            matrix[capacity,g-1] = -data["kapasitas_gudang"][g-1]
            time_rows.append((time,s,g))
    matrix[117] = energy
    upper[117] = settings["batas_emisi_longgar"]
    aggregation = np.zeros((len(groups),n))
    for i, cols in enumerate(groups.values()):
        aggregation[i,cols] = 1
    weights = np.array([probabilities[s] for s,_,_ in groups])
    return Network(matrix,lower,upper,bounds,cost,energy,aggregation,time_rows,names,list(groups),weights)


@dataclass
class Point:
    x: np.ndarray
    value: float
    lower_bound: float
    cost: float
    emission: float
    calls: int
    nodes: int
    solver_seconds: float
    elapsed_seconds: float

    @property
    def warehouses(self):
        return "+".join(f"G{i+1}" for i,y in enumerate(self.x[:4]) if round(y))


class Solver:
    def __init__(self, net, data, nonlinear, pattern=None):
        self.net = net
        settings = data["kontrol_profil"]
        self.alpha = settings["kenaikan_biaya_kuadratik"] if nonlinear else 0
        self.beta = settings["kenaikan_waktu_kuadratik"] if nonlinear else 0
        self.pattern = pattern
        self.n = len(net.names)
        self.aux = len(net.groups) if nonlinear else 0
        self.tangent_points = [set((0.0, 4.0, 8.0, 12.0, 16.0, 20.0)) for _ in range(self.aux)]
        self.linear = np.zeros((len(net.upper),self.n+self.aux))
        self.linear[:,:self.n] = net.linear
        self.cost = np.r_[net.cost, self.alpha*net.weights] if nonlinear else net.cost
        self.emission = np.r_[net.emission, np.zeros(self.aux)]
        for row,s,g in net.time_rows:
            for k,(sg,gg,_) in enumerate(net.groups[:self.aux]):
                if (s,g)==(sg,gg):
                    self.linear[row,self.n+k] = self.beta
        self.integer = np.zeros(self.n + self.aux)
        lb = np.zeros(self.n + self.aux)
        ub = np.r_[net.bounds, np.full(self.aux,np.inf)]
        if pattern is None:
            self.integer[:4] = 1
        else:
            lb[:4] = pattern
            ub[:4] = pattern
        self.bounds = Bounds(lb,ub)

    def tangents(self):
        rows, bounds = [], []
        for k, points in enumerate(self.tangent_points):
            for q in sorted(points):
                row = np.zeros(self.n+self.aux)
                row[:self.n] = 2*q*self.net.aggregation[k]
                row[self.n+k] = -1
                rows.append(row)
                bounds.append(q*q)
        return rows, bounds

    def solve(self, kind, cap=None, cost_cap=None, cutoff=None):
        start = perf_counter()
        calls, nodes, solver_time = 0, 0, 0.0
        objective = self.cost if kind == "cost" else self.emission
        base_upper = self.net.upper.copy()
        if cap is not None:
            base_upper[117] = cap
        fixed_rows, fixed_rhs = [], []
        if cost_cap is not None:
            fixed_rows.append(self.cost)
            fixed_rhs.append(cost_cap)
        if cutoff is not None:
            fixed_rows.append(objective)
            fixed_rhs.append(cutoff)

        for _ in range(140):
            rows, rhs = self.tangents()
            rows += fixed_rows
            rhs += fixed_rhs
            matrix = csr_matrix(np.vstack([self.linear,*rows]))
            lower = np.r_[self.net.lower,np.full(len(rows),-np.inf)]
            upper = np.r_[base_upper,rhs]
            setup = LinearConstraint(matrix, lower, upper)
            t0 = perf_counter()
            result = milp(objective,integrality=self.integer,bounds=self.bounds,
                          constraints=setup,options={"mip_rel_gap": 0})
            solver_time += perf_counter()-t0
            calls += 1
            if result.status == 2:
                raise Infeasible()
            if not result.success:
                raise RuntimeError(result.message)
            nodes += int(getattr(result,"mip_node_count",0) or 0)
            x = result.x[:self.n]
            q = self.net.aggregation @ x
            square = q*q
            activity = self.net.linear @ x
            if self.beta:
                for row,s,g in self.net.time_rows:
                    activity[row] += self.beta*sum(square[k] for k,(sg,gg,_) in enumerate(self.net.groups)
                                                   if (s,g)==(sg,gg))
            charge = float(self.net.cost@x + self.alpha*(self.net.weights@square))
            emission = float(self.net.emission@x)
            value = charge if kind=="cost" else emission
            lower_bound = float(getattr(result,"mip_dual_bound",None) or result.fun)
            valid = (np.all(activity >= self.net.lower-FEAS)
                     and np.all(activity <= base_upper+FEAS)
                     and (cost_cap is None or charge <= cost_cap+FEAS)
                     and np.all(x >= -FEAS) and np.allclose(x[:4],np.round(x[:4]),atol=FEAS,rtol=0))
            if valid and value-lower_bound <= GAP+FEAS:
                return Point(x,value,lower_bound,charge,emission,calls,nodes,solver_time,perf_counter()-start)
            residual = square[:self.aux]-result.x[self.n:]
            added = 0
            for k in np.flatnonzero(residual > 1e-9):
                rounded = round(float(q[k]),11)
                added += int(rounded not in self.tangent_points[k])
                self.tangent_points[k].add(rounded)
            if not added:
                raise RuntimeError(f"Tolerance OA: {kind} cap={cap}, value={value}, lower={lower_bound}, max bound deviation={max(activity-base_upper)}")
        raise RuntimeError(f"Iteration limit, objective={kind}, cap={cap}")


def audit(data, nets, output):
    ref_in = data["level"]["H"]["jalur_masuk"]
    categories = sorted({(g,p) for _,g,p in ref_in})
    ref_out = [(g,j,p) for g,p in categories for j in range(1,7)]
    ref = network(data,ref_in,ref_out,{},False)
    reference = ref.linear != 0
    pairs = list(combinations(range(130),2))
    audited = {}
    fields = ["baris_r","baris_s","bobot_acuan","variabel_bersama_acuan"]
    for level in nets:
        fields += [f"bobot_{level}",f"variabel_bersama_{level}"]
    denom = int(np.triu(reference.astype(int)@reference.astype(int).T,1).sum())
    with output.open("w",newline="",encoding="utf-8") as file:
        writer = DictWriter(file,fieldnames=fields,lineterminator="\n")
        writer.writeheader()
        supports = {}
        for level, models in nets.items():
            first = models["P1"]
            mask = first.linear != 0
            for model in models.values():
                assert model.names == first.names and np.array_equal(mask,model.linear!=0)
            weights = np.triu(mask.astype(int)@mask.astype(int).T,1)
            audited[level] = dict(baris=130,variabel=len(first.names),pasangan_positif=int((weights>0).sum()),
                                  bobot=int(weights.sum()),acuan=denom,wcc=100*int(weights.sum())/denom)
            supports[level] = [{n for n, appears in zip(first.names,row) if appears} for row in mask]
        refs = [{n for n,present in zip(ref.names,row) if present} for row in reference]
        totals = dict.fromkeys(audited,0)
        for r,s in pairs:
            allowed = refs[r]&refs[s]
            row = dict(baris_r=f"R{r+1}",baris_s=f"R{s+1}",bobot_acuan=len(allowed),
                       variabel_bersama_acuan="; ".join(sorted(allowed)))
            for level, supports_by_row in supports.items():
                common = supports_by_row[r]&supports_by_row[s]
                assert common <= allowed
                row[f"bobot_{level}"] = len(common)
                row[f"variabel_bersama_{level}"] = "; ".join(sorted(common))
                totals[level] += len(common)
            writer.writerow(row)
    assert all(totals[l] == a["bobot"] for l,a in audited.items())
    assert [a["bobot"] for a in audited.values()] == [1158,1482,2010] and denom==2370
    return audited


def enumerate_patterns(net,data,nonlinear):
    result = []
    for pattern in PATTERNS:
        try:
            point = Solver(net,data,nonlinear,pattern).solve("cost")
        except Infeasible:
            continue
        result.append((pattern,point))
    return result


def check_enumeration(net,data,nonlinear,kind,point,patterns,cap,cost_cap):
    checked = 0
    valid = 0
    for pattern in patterns:
        fixed = Solver(net,data,nonlinear,pattern)
        try:
            other = fixed.solve(kind,cap,cost_cap,cutoff=point.value+GAP)
        except Infeasible:
            checked += 1
            continue
        assert point.value - other.lower_bound <= 2*GAP+FEAS, (point.value,other.lower_bound)
        checked += 1
        valid += 1
    assert valid > 0
    return checked


def establish(solver, log):
    def solution(kind, stage, cap=None,cost_cap=None):
        point = solver.solve(kind,cap,cost_cap)
        log(stage,kind,point,cap,cost_cap)
        return point
    best_cost = solution("cost","ujung_biaya")
    least_emission_at_best_cost = solution("emission","seri_ujung_biaya",cost_cap=best_cost.cost+TIE)
    least_emission = solution("emission","ujung_emisi")
    best_cost_at_least_emission = solution("cost","seri_ujung_emisi",cap=least_emission.emission+TIE)
    return best_cost,least_emission_at_best_cost,least_emission,best_cost_at_least_emission


def write_csv(path, rows):
    with path.open("w",newline="",encoding="utf-8") as file:
        writer=DictWriter(file,fieldnames=list(rows[0]),lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def run(data_path, output):
    data = json.loads(data_path.read_text())
    output.mkdir(parents=True,exist_ok=True)
    timings, pareto, validation, flows = [],[],[],[]
    nets = {}
    for level,spec in data["level"].items():
        inbound,outbound,demand = (spec[k] for k in ("jalur_masuk","jalur_keluar","permintaan_dasar"))
        assert demand == data["level"]["L"]["permintaan_dasar"]
        nets[level] = {name:network(data,inbound,outbound,demand,stoch)
                       for name,(stoch,_,_) in PROFILES.items()}
    metrics = audit(data,nets,output/"Audit_WCC_Pasangan.csv")
    assert all(nets[l][p].upper[117] == 330 for l in nets for p in PROFILES)
    for level, models in nets.items():
        endpoints, solvers, pattern_sets = {},{},{}
        for profile, (_,multi,nonlinear) in PROFILES.items():
            net = models[profile]
            solvers[profile] = Solver(net,data,nonlinear)
            def log(stage,kind,point,cap=None,cost_cap=None):
                timings.append(dict(tingkat=level,profil=profile,tahap=stage,tujuan=kind,
                    epsilon=cap,batas_biaya=cost_cap,status="optimal_dalam_toleransi",nilai=point.value,
                    batas_bawah=point.lower_bound,panggilan=point.calls,node=point.nodes,
                    solver_detik=point.solver_seconds,total_detik=point.elapsed_seconds))
            if multi:
                endpoints[profile] = establish(solvers[profile],log)
                best = endpoints[profile][0]
            else:
                best = solvers[profile].solve("cost")
                log("optimum_biaya","cost",best)
            enum_start = perf_counter()
            patterns = enumerate_patterns(net,data,nonlinear)
            assert patterns and abs(min(p.cost for _,p in patterns)-best.cost) <= 2*GAP+FEAS
            pattern_sets[profile] = [pattern for pattern,_ in patterns]
            validation.append(dict(tingkat=level,profil=profile,biaya=best.cost,emisi=best.emission,
                gudang=best.warehouses,pola_layak=len(patterns),batas_bawah=best.lower_bound,
                enumerasi_detik=perf_counter()-enum_start))
            print(level,profile,"layak",len(patterns),"biaya",round(best.cost,5),"gudang",best.warehouses,flush=True)

        epsilon_min = max(points[2].emission for points in endpoints.values()) + TIE
        epsilon_max = max(points[1].emission for points in endpoints.values()) + TIE
        assert epsilon_max > epsilon_min
        epsilons = np.linspace(epsilon_min,epsilon_max,data["kontrol_profil"]["jumlah_batas_emisi_bersama"])
        for profile, (_,multi,nonlinear) in PROFILES.items():
            if not multi:
                continue
            net = models[profile]
            solver = solvers[profile]
            def log(stage,kind,point,cap=None,cost_cap=None):
                timings.append(dict(tingkat=level,profil=profile,tahap=stage,tujuan=kind,
                    epsilon=cap,batas_biaya=cost_cap,status="optimal_dalam_toleransi",nilai=point.value,
                    batas_bawah=point.lower_bound,panggilan=point.calls,node=point.nodes,
                    solver_detik=point.solver_seconds,total_detik=point.elapsed_seconds))
            for label, point, kind, cap, cost_cap in [
                ("ujung_emisi",endpoints[profile][3],"cost",endpoints[profile][2].emission+TIE,None),
                ("ujung_biaya",endpoints[profile][1],"emission",None,endpoints[profile][0].cost+TIE),
            ]:
                checked = check_enumeration(net,data,nonlinear,kind,point,pattern_sets[profile],cap,cost_cap)
                pareto.append(dict(tingkat=level,profil=profile,titik=label,epsilon=cap,biaya=point.cost,
                    emisi=point.emission,gudang=point.warehouses,pola_diperiksa=checked))
                for name,value in zip(net.names,point.x):
                    if abs(value)>FEAS:
                        flows.append(dict(tingkat=level,profil=profile,titik=label,variabel=name,nilai=value))
            for i,cap in enumerate(epsilons,1):
                label=f"grid_{i}"
                best = solver.solve("cost",cap)
                log(label,"cost",best,cap)
                point = solver.solve("emission",cap,best.cost+TIE)
                log(f"seri_{label}","emission",point,cap,best.cost+TIE)
                checked = check_enumeration(net,data,nonlinear,"cost",best,pattern_sets[profile],cap,None)
                check_enumeration(net,data,nonlinear,"emission",point,pattern_sets[profile],cap,best.cost+TIE)
                pareto.append(dict(tingkat=level,profil=profile,titik=label,epsilon=cap,biaya=point.cost,
                    emisi=point.emission,gudang=point.warehouses,pola_diperiksa=checked))
                for name,value in zip(net.names,point.x):
                    if abs(value)>FEAS:
                        flows.append(dict(tingkat=level,profil=profile,titik=label,variabel=name,nilai=value))
            print(level,profile,"Pareto",len(epsilons),"batas bersama",flush=True)
    for name,rows in [("Ringkasan",validation),("Pareto",pareto),("Waktu",timings),("Arus_Pareto",flows)]:
        write_csv(output/f"{name}.csv",rows)
    meta = dict(gap_oa=GAP,toleransi_kelayakan=FEAS,toleransi_seri=TIE,
                python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,
                sistem=platform.system(),arsitektur=platform.machine(),wcc=metrics)
    (output/"Ringkasan_WCC.json").write_text(json.dumps(meta,ensure_ascii=False,indent=2)+"\n")
    return meta


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--data",type=Path,default=Path(__file__).resolve().parents[1]/"case/Data_Bersama.json")
    parser.add_argument("--hasil",type=Path,default=Path("hasil_verifikasi"))
    opts = parser.parse_args()
    print(json.dumps(run(opts.data,opts.hasil),ensure_ascii=False))
