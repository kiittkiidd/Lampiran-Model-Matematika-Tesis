"""Independent validation from route dictionaries, without the solver matrix."""
from pathlib import Path
from itertools import product
import json,gzip,numpy as np
from network import PROFILES
ROOT=Path(__file__).parent
CONFIG=json.loads((ROOT/'config.json').read_text())

def check_record(record,data):
    stochastic,multi,nonlinear=PROFILES[record['profile']];spec=data['level'][record['level']]
    incoming=spec['jalur_masuk'];outgoing=spec['jalur_keluar'];base=spec['permintaan_dasar']
    scenarios=data['P2']['skenario'] if stochastic else [{'peluang':1.,'pengali':dict(A=1.,B=1.,C=1.)}]
    maximum_violation=objective_error=0.;points=record['points']
    assert len(points)==(25 if multi else 1)
    for point in points:
        vector=point['vector'];assert all(np.isfinite(v) for v in vector)
        assert np.isfinite(point['cost']) and np.isfinite(point['emission'])
        assert len(vector)==4+len(scenarios)*(len(incoming)+len(outgoing))
        y=vector[:4];violation=max(0.,-min(vector),max(abs(v-round(v)) for v in y),max(y)-1.)
        cost=sum(v*f for v,f in zip(y,data['biaya_buka_gudang']));emission=sum(v*f for v,f in zip(y,data['P3']['emisi_tetap_gudang']))
        for ss,scene in enumerate(scenarios):
            offset=4+ss*(len(incoming)+len(outgoing));xs=dict(zip(map(tuple,incoming),vector[offset:offset+len(incoming)]));zs=dict(zip(map(tuple,outgoing),vector[offset+len(incoming):offset+len(incoming)+len(outgoing)]));probability=scene['peluang']
            q={(g,p):sum(v for (gg,j,pp),v in zs.items() if (gg,pp)==(g,p)) for g,p in product(range(1,5),'ABC')}
            for (g,p),amount in q.items():violation=max(violation,abs(sum(v for (i,gg,pp),v in xs.items() if (gg,pp)==(g,p))-amount))
            for j,p in product(range(1,7),'ABC'):
                demand=base[f'{j},{p}']*scene['pengali'][p]
                violation=max(violation,abs(sum(v for (g,jj,pp),v in zs.items() if (jj,pp)==(j,p))-demand))
            for g in range(1,5):
                total=sum(q[g,p] for p in 'ABC');square=sum(q[g,p]**2 for p in 'ABC');hours=total+(data['kontrol_profil']['kenaikan_waktu_kuadratik']*square if nonlinear else 0.)
                violation=max(violation,total-data['kapasitas_gudang'][g-1]*y[g-1],hours-data['kontrol_profil']['waktu_gudang'][g-1]*y[g-1])
            cost+=probability*(sum(v*data['tarif_masuk_per_ton'][i-1][g-1] for (i,g,p),v in xs.items())+sum(v*(data['tarif_keluar_per_ton'][g-1][j-1]+data['tarif_penanganan_per_ton'][g-1]['ABC'.index(p)]) for (g,j,p),v in zs.items())+(data['kontrol_profil']['kenaikan_biaya_kuadratik']*sum(v*v for v in q.values()) if nonlinear else 0.))
            emission+=probability*(sum(v*data['P3']['emisi_masuk_per_ton'][i-1][g-1] for (i,g,p),v in xs.items())+sum(v*data['P3']['emisi_keluar_per_ton'][g-1][j-1] for (g,j,p),v in zs.items()))
        if 'epsilon' in point:violation=max(violation,emission-point['epsilon'])
        objective_error=max(objective_error,abs(cost-point['cost']),abs(emission-point['emission']));maximum_violation=max(maximum_violation,violation)
    assert maximum_violation<=CONFIG['constraint_check_tolerance'],(record['profile'],record['level'],maximum_violation)
    assert objective_error<=1e-7,objective_error
    assert record['calls']==(50 if multi else 1)
    assert record['lp_iterations']==sum(s['lp_iterations'] for s in record['steps'])
    assert record['nodes']==sum(s['nodes'] for s in record['steps'])
    assert abs(record['solver_seconds']-sum(s['solver_seconds'] for s in record['steps']))<1e-9
    assert all(s['status'] in ('optimal','gaplimit') for s in record['steps'])
    assert all(s['gap']<=0.000251 for s in record['steps'])
    return dict(profile=record['profile'],level=record['level'],points=len(points),max_violation=maximum_violation,max_objective_error=objective_error)

def main():
    data=json.loads((ROOT/'data.json').read_text());results_path=ROOT/'benchmark_runs.jsonl'
    if not results_path.exists():results_path=ROOT.parent/'hasil'/'benchmark_runs.jsonl'
    if not results_path.exists() and results_path.with_suffix(results_path.suffix+'.gz').exists():results_path=results_path.with_suffix(results_path.suffix+'.gz')
    contents=gzip.decompress(results_path.read_bytes()).decode('utf-8') if results_path.suffix=='.gz' else results_path.read_text()
    records=[json.loads(a) for a in contents.splitlines()]
    report=[check_record(r,data) for r in records]
    references=json.loads((ROOT/'reference_costs.json').read_text());matched=[]
    for record in records:
        stochastic,multi,nonlinear=PROFILES[record['profile']]
        reference=next(x for x in references if (x['level'],x['stochastic'],x['nonlinear'])==(record['level'],stochastic,nonlinear))
        lower=max(record['steps'][0]['dual_bound'],reference['cost_lower']);upper=min(record['cost_min'],reference['cost_upper'])
        assert lower<=upper+1e-5,(record['profile'],record['level'],lower,upper)
        matched.append(abs(record['cost_min']-reference['cost_upper']))
    output=dict(reference_cost_checks=len(matched),max_reference_cost_difference=max(matched,default=0.),records=len(report),points=sum(a['points'] for a in report),max_violation=max((a['max_violation'] for a in report),default=0.),max_objective_error=max((a['max_objective_error'] for a in report),default=0.),checks=report)
    (results_path.parent/'validation.json').write_text(json.dumps(output,indent=2));print({k:v for k,v in output.items() if k!='checks'})
if __name__=='__main__':main()
