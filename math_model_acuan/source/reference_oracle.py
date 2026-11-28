"""Independent minimum-cost oracle: enumerate warehouse patterns, then scenarios.
Factory flows are eliminated analytically because each eligible factory has
unlimited supply. A different (direct quadratic epigraph) SCIP formulation is used.
This oracle is not included in the benchmark timing.
"""
from pathlib import Path
from itertools import product
from time import perf_counter
import json,numpy as np
from pyscipopt import Model,quicksum
ROOT=Path(__file__).parent
DATA=json.loads((ROOT/'data.json').read_text())
TOL=2.5e-5

def scenario_cost(data,level,pattern,scene,nonlinear):
    spec=data['level'][level];arcs=[tuple(v) for v in spec['jalur_keluar'] if pattern[v[0]-1]]
    demand={(j,p):spec['permintaan_dasar'][f'{j},{p}']*scene['pengali'][p] for j,p in product(range(1,7),'ABC')}
    if any(not any((jj,pp)==(j,p) for g,jj,pp in arcs) for j,p in demand):return None
    inbound={(g,p):min(data['tarif_masuk_per_ton'][i-1][g-1] for i,gg,pp in spec['jalur_masuk'] if (gg,pp)==(g,p)) for g,p in product(range(1,5),'ABC')}
    m=Model();m.hideOutput();m.setParam('parallel/maxnthreads',1);m.setParam('lp/threads',1);m.setParam('constraints/nonlinear/assumeconvex',True);m.setParam('numerics/feastol',1e-9);m.setParam('limits/gap',0.);m.setParam('limits/absgap',TOL if nonlinear else 1e-9);m.setParam('limits/time',30.)
    z={key:m.addVar(name=f'z{key}',lb=0,ub=demand[key[1],key[2]]) for key in arcs}
    q={(g,p):quicksum(v for (gg,j,pp),v in z.items() if (gg,pp)==(g,p)) for g,p in product(range(1,5),'ABC')}
    for (j,p),value in demand.items():m.addCons(quicksum(v for (g,jj,pp),v in z.items() if (jj,pp)==(j,p))==value)
    for g in range(1,5):
        if not pattern[g-1]:continue
        total=quicksum(q[g,p] for p in 'ABC');m.addCons(total<=data['kapasitas_gudang'][g-1])
        hours=total+(data['kontrol_profil']['kenaikan_waktu_kuadratik']*quicksum(q[g,p]*q[g,p] for p in 'ABC') if nonlinear else 0.)
        m.addCons(hours<=data['kontrol_profil']['waktu_gudang'][g-1])
    cost=quicksum((inbound[g,p]+data['tarif_penanganan_per_ton'][g-1]['ABC'.index(p)]+data['tarif_keluar_per_ton'][g-1][j-1])*v for (g,j,p),v in z.items())
    if nonlinear:
        cost+=data['kontrol_profil']['kenaikan_biaya_kuadratik']*quicksum(value*value for value in q.values());t=m.addVar('cost_epigraph',lb=0);m.addCons(cost<=t);m.setObjective(t)
    else:m.setObjective(cost)
    m.optimize();status=str(m.getStatus())
    if status=='infeasible':m.freeProb();return None
    if status not in ('optimal','gaplimit') or m.getNSols()==0:raise RuntimeError((level,pattern,status))
    amounts={k:m.getVal(v) for k,v in z.items()};totals={(g,p):sum(v for (gg,j,pp),v in amounts.items() if (gg,pp)==(g,p)) for g,p in product(range(1,5),'ABC')}
    value=sum((inbound[g,p]+data['tarif_penanganan_per_ton'][g-1]['ABC'.index(p)]+data['tarif_keluar_per_ton'][g-1][j-1])*v for (g,j,p),v in amounts.items())
    if nonlinear:value+=data['kontrol_profil']['kenaikan_biaya_kuadratik']*sum(q*q for q in totals.values())
    lower=float(m.getDualbound());assert -1e-5<=value-lower<=TOL+1e-5,(level,pattern,value-lower)
    m.freeProb();return value,lower

def reference(data,level,stochastic,nonlinear):
    scenes=data['P2']['skenario'] if stochastic else [{'peluang':1.,'pengali':dict(A=1,B=1,C=1)}]
    total=[sum(data['level'][level]['permintaan_dasar'][f'{j},{p}']*s['pengali'][p] for j,p in product(range(1,7),'ABC')) for s in scenes]
    upper=np.inf;lower=np.inf;winner=None;feasible=0
    for pattern in product((0,1),repeat=4):
        if sum(v*y for v,y in zip(data['kapasitas_gudang'],pattern))<max(total)-1e-10:continue
        constant=sum(f*y for f,y in zip(data['biaya_buka_gudang'],pattern));u=l=constant
        for scene in scenes:
            result=scenario_cost(data,level,pattern,scene,nonlinear)
            if result is None:break
            us,ls=result;u+=scene['peluang']*us;l+=scene['peluang']*ls
        else:
            feasible+=1;lower=min(lower,l)
            if u<upper:upper=u;winner=[i+1 for i,y in enumerate(pattern) if y]
    assert np.isfinite(upper) and upper-lower<=TOL+1e-5
    return dict(level=level,stochastic=stochastic,nonlinear=nonlinear,cost_upper=upper,cost_lower=lower,gap=upper-lower,warehouses=winner,feasible_patterns=feasible)

if __name__=='__main__':
    results=[];start=perf_counter()
    for p,st,nl in [('P1',False,False),('P2',True,False),('P5',False,True),('P6',True,True)]:
        for level in 'LMH':
            r=reference(DATA,level,st,nl);r['profile']=p;results.append(r);(ROOT/'reference_costs.json').write_text(json.dumps(results,indent=2));print(r,flush=True)
    print('Verification seconds (excluded from benchmark):',perf_counter()-start)
