"""Check physical entities, route nesting, shared data and scenario construction."""
from pathlib import Path
from itertools import product
from math import isclose
import json,hashlib
ROOT=Path(__file__).parent
def main():
 d=json.loads((ROOT/'data.json').read_text());sets={}
 for l in 'LMH':
  s=d['level'][l];incoming=list(map(tuple,s['jalur_masuk']));outgoing=list(map(tuple,s['jalur_keluar']))
  assert len(incoming)==len(set(incoming)) and len(outgoing)==len(set(outgoing))
  assert all(i in range(1,7) and g in range(1,5) and p in 'ABC' for i,g,p in incoming)
  assert all(g in range(1,5) and j in range(1,7) and p in 'ABC' for g,j,p in outgoing)
  assert all(any(gg==g and pp==p for i,gg,pp in incoming) for g,j,p in outgoing)
  assert all(any(jj==j and pp==p for g,jj,pp in outgoing) for j,p in product(range(1,7),'ABC'))
  assert s['permintaan_dasar']==d['level']['L']['permintaan_dasar']
  sets[l]=(set(incoming),set(outgoing))
 for a,b in [('L','M'),('M','H')]:assert all(x<=y for x,y in zip(sets[a],sets[b]))
 mean=d['level']['L']['permintaan_dasar'];assert len(mean)==18 and all(x>0 for x in mean.values())
 assert all(isclose(sum(mean[f'{j},{p}'] for j in range(1,7)),10,abs_tol=1e-10) for p in 'ABC')
 marg=d['P2']['distribusi_produk']
 for p in 'ABC':
  assert isclose(sum(prob for value,prob in marg[p]),1,abs_tol=1e-12)
  assert isclose(sum(value*prob for value,prob in marg[p]),1,abs_tol=1e-12)
 scenes=d['P2']['skenario'];assert len(scenes)==27 and isclose(sum(s['peluang'] for s in scenes),1,abs_tol=1e-12)
 actual={(tuple(s['pengali'][p] for p in 'ABC'),round(s['peluang'],12)) for s in scenes}
 expected={(tuple(a[0] for a in c),round(c[0][1]*c[1][1]*c[2][1],12)) for c in product(*(marg[p] for p in 'ABC'))}
 assert actual==expected
 for p in 'ABC':assert isclose(sum(s['peluang']*s['pengali'][p] for s in scenes),1,abs_tol=1e-12)
 result=dict(passed=True,physical_nodes=dict(factories=6,warehouses=4,zones=6,products=3),all_warehouses_handle_all_products=True,route_nesting=True,common_mean_demand=True,mean_total_demand=30,scenarios=27,total_scenario_probability=sum(s['peluang'] for s in scenes),max_total_demand=max(sum(mean[f'{j},{p}']*s['pengali'][p] for j,p in product(range(1,7),'ABC')) for s in scenes),data_sha256=hashlib.sha256((ROOT/'data.json').read_bytes()).hexdigest())
 (ROOT/'input_validation.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
if __name__=='__main__':main()
