"""Default SCIP implementation: joint binary/continuous optimization for P1–P8."""
from pathlib import Path
from time import perf_counter
import json
from tempfile import NamedTemporaryFile
import numpy as np
from pyscipopt import Model, quicksum
from network import PROFILES, network
ROOT=Path(__file__).parent
CONFIG=json.loads((ROOT/'config.json').read_text())
DATA=json.loads((ROOT/'data.json').read_text())

class SCIPNetwork:
    def __init__(self,data,level,stochastic,nonlinear):
        self.data=data;self.level=level;self.stochastic=stochastic;self.nonlinear=nonlinear
        spec=data['level'][level]
        self.net=network(data,spec['jalur_masuk'],spec['jalur_keluar'],spec['permintaan_dasar'],stochastic)
        self.steps=[];self.solution_pool=[]

    def solve(self,goal,emission_limit=None,cost_limit=None):
        start=perf_counter();net=self.net;m=Model();m.hideOutput()
        for name,value in {'parallel/maxnthreads':CONFIG['threads'],'lp/threads':CONFIG['threads'],'randomization/randomseedshift':CONFIG['random_seed'],'randomization/permutationseed':CONFIG['random_seed'],'randomization/lpseed':CONFIG['random_seed'],'constraints/nonlinear/assumeconvex':CONFIG['nonlinear_assumeconvex'],'limits/gap':0.,'limits/absgap':CONFIG['objective_gap_cost'] if goal=='C' and self.nonlinear else CONFIG['objective_gap_emission'] if goal=='E' and self.nonlinear else 1e-8,'numerics/feastol':CONFIG['scip_feasibility_tolerance'],'limits/time':float(CONFIG['scalar_time_limit_seconds'])}.items():m.setParam(name,value)
        version=f'{m.getMajorVersion()}.{m.getMinorVersion()}.{m.getTechVersion()}'
        assert version==CONFIG['expected_scip_version'],version
        # Exact solver representation: finite bounds follow from nonnegative flows,
        # demand equalities, warehouse capacity and the conservation equations.
        spec=self.data['level'][self.level]
        scenarios=self.data['P2']['skenario'] if self.stochastic else [{'peluang':1,'pengali':dict(A=1,B=1,C=1)}]
        demand={(ss,j,p):spec['permintaan_dasar'][f'{j},{p}']*scene['pengali'][p] for ss,scene in enumerate(scenarios) for j in range(1,7) for p in 'ABC'}
        product_demand={(ss,p):sum(demand[ss,j,p] for j in range(1,7)) for ss in range(len(scenarios)) for p in 'ABC'}
        variables=[]
        for j,name in enumerate(net.names):
            if j<4:upper=1.
            else:
                a,b,p,ss=name[2:-1].split(',');a=int(a);b=int(b);ss=int(ss)-1;g=b if name.startswith('x') else a
                upper=min(self.data['kapasitas_gudang'][g-1],product_demand[ss,p] if name.startswith('x') else demand[ss,b,p])
            variables.append(m.addVar(name=name,lb=0,ub=float(upper),vtype='B' if j<4 else 'C'))
        groups=[]
        for k,row in enumerate(net.aggregation):
            ss,g,p=net.groups[k]
            throughput=m.addVar(name=f'solver_only_throughput[{ss+1},{g},{p}]',lb=0,ub=min(self.data['kapasitas_gudang'][g-1],product_demand[ss,p]))
            m.markDoNotAggrVar(throughput)
            m.addCons(throughput==quicksum(variables[j] for j in np.flatnonzero(row)))
            groups.append(throughput)
        squares=[]
        if self.nonlinear:
            for k,throughput in enumerate(groups):
                ss,g,p=net.groups[k];maximum=min(self.data['kapasitas_gudang'][g-1],product_demand[ss,p])
                square=m.addVar(name=f'solver_only_square[{ss+1},{g},{p}]',lb=0,ub=maximum*maximum)
                m.markDoNotAggrVar(square)
                m.addCons(throughput*throughput<=square)
                squares.append(square)
        time_rows={r:(ss,g) for r,ss,g in net.time_rows}
        for row,coefficients in enumerate(net.linear):
            if row in time_rows and self.nonlinear:
                scenario,g=time_rows[row];indices=[k for k,(ss,gg,p) in enumerate(net.groups) if (ss,gg)==(scenario,g)]
                hours=quicksum(groups[k]+self.data['kontrol_profil']['kenaikan_waktu_kuadratik']*squares[k] for k in indices)
                m.addCons(hours<=self.data['kontrol_profil']['waktu_gudang'][g-1]*variables[g-1]);continue
            expression=quicksum(float(coefficients[j])*variables[j] for j in np.flatnonzero(coefficients));lo,hi=net.lower[row],net.upper[row]
            if lo==hi:m.addCons(expression==float(hi))
            else:
                if np.isfinite(lo):m.addCons(expression>=float(lo))
                if np.isfinite(hi):m.addCons(expression<=float(hi))
        cost=quicksum(float(c)*v for c,v in zip(net.cost,variables))
        if self.nonlinear:cost+=self.data['kontrol_profil']['kenaikan_biaya_kuadratik']*quicksum(float(w)*v for w,v in zip(net.weights,squares))
        emission=quicksum(float(e)*v for e,v in zip(net.emission,variables))
        if emission_limit is not None:m.addCons(emission<=float(emission_limit))
        if cost_limit is not None:m.addCons(cost<=float(cost_limit))
        objective=None
        m.setObjective(cost if goal=='C' else emission,'minimize')
        candidates=[p for p in self.solution_pool if (emission_limit is None or p['emission']<=emission_limit+1e-9) and (cost_limit is None or p['cost']<=cost_limit+1e-9)]
        if candidates:
            candidate=min(candidates,key=lambda p:p['cost' if goal=='C' else 'emission']);initial=m.createSol()
            for variable,value in zip(variables,candidate['vector']):m.setSolVal(initial,variable,float(value))
            qstart=net.aggregation@np.asarray(candidate['vector'])
            for variable,value in zip(groups,qstart):m.setSolVal(initial,variable,float(value))
            for variable,value in zip(squares,qstart):m.setSolVal(initial,variable,float(value*value))
            if objective is not None:m.setSolVal(initial,objective,candidate['cost']+1e-8)
            m.addSol(initial,free=True)
        model_seconds=perf_counter()-start;optimize_start=perf_counter();m.optimize();optimize_wall=perf_counter()-optimize_start
        info=dict(step=len(self.steps)+1,goal=goal,emission_limit=emission_limit,cost_limit=cost_limit,status=str(m.getStatus()),solver_seconds=float(m.getSolvingTime()),presolve_seconds=float(m.getPresolvingTime()),model_seconds=model_seconds,optimize_wall_seconds=optimize_wall,lp_iterations=int(m.getNLPIterations()),lp_solves=int(m.getNLPs()),nodes=int(m.getNNodes()),deterministic_work=float(m.getDeterministicTime()),dual_bound=float(m.getDualbound()))
        with NamedTemporaryFile(suffix='.json') as statistics_file:
            m.writeStatisticsJson(statistics_file.name)
            statistics=json.loads(Path(statistics_file.name).read_text())
        nlpi=statistics.get('nlpi',{}).get('nlp_solvers',{})
        info['nlp_statistics']=nlpi
        if m.getNSols()==0:self.steps.append(info);raise RuntimeError(dict(level=self.level,stochastic=self.stochastic,nonlinear=self.nonlinear,error='no feasible solution',**info))
        x=np.array([m.getVal(v) for v in variables]);q=net.aggregation@x
        true_cost=float(net.cost@x+(self.data['kontrol_profil']['kenaikan_biaya_kuadratik']*(net.weights@(q*q)) if self.nonlinear else 0));true_emission=float(net.emission@x)
        rows=net.linear@x
        if self.nonlinear:
            for row,(ss,g) in time_rows.items():rows[row]+=self.data['kontrol_profil']['kenaikan_waktu_kuadratik']*sum(q[k]**2 for k,(s,gg,p) in enumerate(net.groups) if (s,gg)==(ss,g))
        finite=np.isfinite(net.lower);violation=max(float(np.max(rows-net.upper)),float(np.max(net.lower[finite]-rows[finite])),float(np.max(-x)),float(np.max(abs(x[:4]-np.round(x[:4])))))
        if emission_limit is not None:violation=max(violation,true_emission-emission_limit)
        if cost_limit is not None:violation=max(violation,true_cost-cost_limit)
        value=true_cost if goal=='C' else true_emission;gap=value-info['dual_bound'];info.update(cost=true_cost,emission=true_emission,gap=gap,max_violation=violation)
        self.steps.append(info)
        if violation>CONFIG['constraint_check_tolerance'] or gap>CONFIG['objective_gap_cost' if goal=='C' else 'objective_gap_emission']+CONFIG['constraint_check_tolerance'] or gap<-CONFIG['constraint_check_tolerance']:
            raise RuntimeError(dict(level=self.level,stochastic=self.stochastic,nonlinear=self.nonlinear,error='numerical certificate failed',**info))
        result=dict(cost=true_cost,emission=true_emission,warehouses=(np.flatnonzero(x[:4]>.5)+1).tolist(),gap=gap,status=info['status'],vector=x.tolist())
        self.solution_pool.append(result);m.freeProb();return result

def run(profile,level,data=None,progress=None):
    start=perf_counter();stochastic,multi,nonlinear=PROFILES[profile];model=SCIPNetwork(DATA if data is None else data,level,stochastic,nonlinear)
    def solve(*args,**kwargs):
        result=model.solve(*args,**kwargs)
        if progress:progress(model.steps[-1])
        return result
    minimum_cost=solve('C');points=[minimum_cost]
    if multi:
        minimum_emission=solve('E');left=solve('C',emission_limit=minimum_emission['emission']+CONFIG['objective_gap_emission']);right=solve('E',cost_limit=minimum_cost['cost']+CONFIG['lexicographic_cost_tolerance'])
        limits=np.linspace(left['emission'],right['emission'],CONFIG['pareto_grid_points']);points=[dict(**left,epsilon=float(limits[0]))]
        for limit in limits[1:-1]:
            c=solve('C',emission_limit=float(limit));p=solve('E',emission_limit=float(limit),cost_limit=c['cost']+CONFIG['lexicographic_cost_tolerance']);points.append(dict(**p,epsilon=float(limit)))
        points.append(dict(**right,epsilon=float(limits[-1])))
    tolerance=2*CONFIG['lexicographic_cost_tolerance']+CONFIG['constraint_check_tolerance'];unique=[]
    for point in points:
        if not any(abs(point['cost']-a['cost'])<=tolerance and abs(point['emission']-a['emission'])<=tolerance for a in unique):unique.append(point)
    frontier=[p for p in unique if not any(a['cost']<=p['cost']+tolerance and a['emission']<=p['emission']+tolerance and (a['cost']<p['cost']-tolerance or a['emission']<p['emission']-tolerance) for a in unique)]
    return dict(profile=profile,level=level,cost_min=minimum_cost['cost'],cost_min_emission=minimum_cost['emission'],warehouses=minimum_cost['warehouses'],points=points,frontier=frontier,steps=model.steps,calls=len(model.steps),lp_iterations=sum(s['lp_iterations'] for s in model.steps),lp_solves=sum(s['lp_solves'] for s in model.steps),nodes=sum(s['nodes'] for s in model.steps),solver_seconds=sum(s['solver_seconds'] for s in model.steps),presolve_seconds=sum(s['presolve_seconds'] for s in model.steps),model_seconds=sum(s['model_seconds'] for s in model.steps),total_seconds=perf_counter()-start,max_violation=max(s['max_violation'] for s in model.steps),max_gap=max(s['gap'] for s in model.steps))

if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser();parser.add_argument('--profile',choices=PROFILES,default='P1');parser.add_argument('--level',choices=list('LMH'),default='L');parser.add_argument('--output',type=Path);args=parser.parse_args()
    def progress(s):print(f"{args.profile} {args.level} step {s['step']} {s['goal']} {s['status']} solver={s['solver_seconds']:.4f}s LP={s['lp_iterations']}",flush=True)
    result=run(args.profile,args.level,progress=progress)
    if args.output:args.output.write_text(json.dumps(result))
    print(json.dumps({k:v for k,v in result.items() if k not in ('steps','points','frontier')}))
