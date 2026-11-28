"""Audit semantic row supports and WCC independently of SCIP transformations."""
from pathlib import Path
from itertools import product,combinations
from collections import Counter
import json,csv,numpy as np
from network import network,PROFILES
ROOT=Path(__file__).parent
d=json.loads((ROOT/'data.json').read_text());levels={**d['level'],'REF':dict(jalur_masuk=d['level']['H']['jalur_masuk'],jalur_keluar=list(product(range(1,5),range(1,7),'ABC')),permintaan_dasar=d['level']['L']['permintaan_dasar'])}
def direct(spec):
 incoming={f'x[{i},{g},{p}]':(i,g,p) for i,g,p in spec['jalur_masuk']};outgoing={f'z[{g},{j},{p}]':(g,j,p) for g,j,p in spec['jalur_keluar']}
 rows=[{v for v,(i,gg,pp) in incoming.items() if (gg,pp)==(g,p)}|{v for v,(gg,j,pp) in outgoing.items() if (gg,pp)==(g,p)} for g,p in product(range(1,5),'ABC')]
 rows += [{v for v,(g,jj,pp) in outgoing.items() if (jj,pp)==(j,p)} for j,p in product(range(1,7),'ABC')]
 caps=[{v for v,(gg,j,p) in outgoing.items() if gg==g}|{f'y[{g}]'} for g in range(1,5)]
 return rows+caps+caps
supports={l:direct(s) for l,s in levels.items()};reference=supports['REF'];summary={}
for l in 'LMH':
 spec=levels[l];actual=supports[l]
 for profile,(st,multi,nl) in PROFILES.items():
  n=network(d,spec['jalur_masuk'],spec['jalur_keluar'],spec['permintaan_dasar'],st)
  for ss in range(27 if st else 1):
   indices=list(range(ss*34,(ss+1)*34))+[row for row,s,g in n.time_rows if s==ss]
   matrix=[{n.names[c].rsplit(',',1)[0]+']' if c>=4 else n.names[c] for c in np.flatnonzero(n.linear[row])} for row in indices]
   assert matrix==actual,(l,profile,ss)
 a=sum(len(u&v) for u,v in combinations(actual,2));oc=Counter(x for row in actual for x in row);assert a==sum(v*(v-1)//2 for v in oc.values());b=sum(len(u&v) for u,v in combinations(reference,2));assert all(s<=ref for s,ref in zip(actual,reference))
 summary[l]=dict(rows=38,pairs=703,inbound=len(spec['jalur_masuk']),outbound=len(spec['jalur_keluar']),numerator=a,denominator=b,wcc=100*a/b,business_variables_deterministic=4+len(spec['jalur_masuk'])+len(spec['jalur_keluar']),business_variables_stochastic=4+27*(len(spec['jalur_masuk'])+len(spec['jalur_keluar'])))
 assert a==4+6*len(spec['jalur_keluar']) and b==436
out=ROOT/'audit';out.mkdir(exist_ok=True);(out/'WCC.json').write_text(json.dumps(summary,indent=2))
with (out/'WCC_Pasangan.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['Baris_1','Baris_2','Variabel_pembanding','Bobot_pembanding','Variabel_Low','Bobot_Low','Variabel_Medium','Bobot_Medium','Variabel_High','Bobot_High'])
 for i,j in combinations(range(38),2):
  row=[f'R{i+1}',f'R{j+1}'];shared=reference[i]&reference[j];row.extend(['; '.join(sorted(shared)),len(shared)])
  for l in 'LMH':shared=supports[l][i]&supports[l][j];row.extend(['; '.join(sorted(shared)),len(shared)])
  w.writerow(row)
with (out/'WCC_Baris.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['Tingkat','Baris','NNZ_dukungan_variabel','Variabel'])
 for l,rows in supports.items():
  for i,row in enumerate(rows,1):w.writerow([l,f'R{i}',len(row),'; '.join(sorted(row))])
print(json.dumps(summary,indent=2))
