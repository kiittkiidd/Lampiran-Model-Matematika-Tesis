from pathlib import Path
from collections import defaultdict
from statistics import median
import json,csv
from verify import check_record
ROOT=Path(__file__).parent

def main():
 records=[json.loads(s) for s in (ROOT/'validation_variants.jsonl').read_text().splitlines()];groups=defaultdict(list);checks=[]
 for r in records:
  d=json.loads((ROOT/f"validation_data_{r['variant']}.json").read_text());checks.append(check_record(r,d));groups[r['variant'],r['profile'],r['level']].append(r)
 protocol=json.loads((ROOT/'calibration_protocol.json').read_text());expected=len(protocol['heldout_seeds'])*len(protocol['heldout_profiles'])*3*protocol['repetitions_per_heldout_case'];assert len(records)==expected
 rows=[];trends=[]
 for key,rs in sorted(groups.items()):
  assert len(rs)==3;seed,p,l=key;rows.append(dict(variant=seed,profile=p,level=l,solver_seconds_median=median(r['solver_seconds'] for r in rs),lp_iterations_median=median(r['lp_iterations'] for r in rs)))
 for seed in protocol['heldout_seeds']:
  for p in protocol['heldout_profiles']:
   rs=[next(r for r in rows if (r['variant'],r['profile'],r['level'])==(seed,p,l)) for l in 'LMH'];trends.append(dict(variant=seed,profile=p,time_ordered=rs[0]['solver_seconds_median']<rs[1]['solver_seconds_median']<rs[2]['solver_seconds_median'],lp_ordered=rs[0]['lp_iterations_median']<rs[1]['lp_iterations_median']<rs[2]['lp_iterations_median']))
 t=sum(x['time_ordered'] for x in trends);lp=sum(x['lp_ordered'] for x in trends)
 narrative=f'Urutan median waktu Low < Medium < High ditemukan pada {t} dari {len(trends)} perbandingan profil–variasi. Urutan iterasi LP ditemukan pada {lp} dari {len(trends)} perbandingan. '
 failed=[f"{x['profile']} pada variasi {x['variant']}" for x in trends if not x['time_ordered']];failedlp=[f"{x['profile']} pada variasi {x['variant']}" for x in trends if not x['lp_ordered']]
 if failed:narrative+='Pengecualian waktu: '+', '.join(failed)+'. '
 if failedlp:narrative+='Pengecualian iterasi LP: '+', '.join(failedlp)+'. '
 narrative+='Pengukuran ini menilai sensitivitas terhadap perubahan data. Kesimpulan urutan pada data acuan tidak diperluas menjadi jaminan untuk setiap variasi permintaan.'
 result=dict(records=len(records),rows=rows,trends=trends,time_ordered=t,lp_ordered=lp,comparisons=len(trends),max_violation=max(c['max_violation'] for c in checks),max_objective_error=max(c['max_objective_error'] for c in checks),narrative=narrative)
 (ROOT/'validation_variants_summary.json').write_text(json.dumps(result,indent=2))
 with (ROOT/'Sensitivitas.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 print(narrative)
if __name__=='__main__':main()
