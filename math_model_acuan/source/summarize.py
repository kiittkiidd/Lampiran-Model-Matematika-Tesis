"""Summarize only completed SCIP benchmark runs; retain every measurement."""
from pathlib import Path
from statistics import median
from collections import defaultdict
import csv,json
ROOT=Path(__file__).parent
CONFIG=json.loads((ROOT/'config.json').read_text())

def nlp_values(step):
    values=step.get('nlp_statistics',{}).values()
    return dict(iterations=sum(v.get('iterations',0) for v in values),solves=sum(v.get('solves',0) for v in values),seconds=sum(v.get('solve_time',0.) for v in values))

def main():
    records=[json.loads(line) for line in (ROOT/'benchmark_runs.jsonl').read_text().splitlines()];groups=defaultdict(list)
    for record in records:groups[record['profile'],record['level']].append(record)
    assert len(groups)==24 and len(records)==24*CONFIG['benchmark_repeats']
    rows=[]
    for p in [f'P{i}' for i in range(1,9)]:
        for level in 'LMH':
            a=groups[p,level];assert len(a)==CONFIG['benchmark_repeats']
            nlp=[sum(nlp_values(s)['iterations'] for s in x['steps']) for x in a]
            rows.append(dict(profile=p,level=level,repeats=len(a),calls=a[0]['calls'],cost_min_median=median(x['cost_min'] for x in a),solver_ms_median=1000*median(x['solver_seconds'] for x in a),solver_ms_min=1000*min(x['solver_seconds'] for x in a),solver_ms_max=1000*max(x['solver_seconds'] for x in a),total_ms_median=1000*median(x['total_seconds'] for x in a),model_ms_median=1000*median(x['model_seconds'] for x in a),presolve_ms_median=1000*median(x['presolve_seconds'] for x in a),lp_iterations_median=median(x['lp_iterations'] for x in a),lp_iterations_min=min(x['lp_iterations'] for x in a),lp_iterations_max=max(x['lp_iterations'] for x in a),nlp_iterations_median=median(nlp),nodes_median=median(x['nodes'] for x in a),lp_solves_median=median(x['lp_solves'] for x in a),pareto_points_reference=len(a[0]['frontier']),warehouses_cost_min_reference=a[0]['warehouses'],max_violation=max(x['max_violation'] for x in a),max_gap=max(x['max_gap'] for x in a)))
    with (ROOT/'Benchmark.csv').open('w',newline='') as f:
        keys=['repeat','profile','level','calls','solver_seconds','total_seconds','model_seconds','presolve_seconds','lp_iterations','lp_solves','nodes','nlp_iterations','cost_min','max_violation','max_gap']
        writer=csv.DictWriter(f,fieldnames=keys);writer.writeheader()
        for record in records:
            row={k:record.get(k) for k in keys};row['nlp_iterations']=sum(nlp_values(step)['iterations'] for step in record['steps']);writer.writerow(row)
    (ROOT/'summary.json').write_text(json.dumps(rows,indent=2))
    with (ROOT/'Ringkasan.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    with (ROOT/'Waktu_dan_Iterasi_Per_Langkah.csv').open('w',newline='') as f:
        keys=['repeat','profile','level','step','goal','emission_limit','cost_limit','status','solver_seconds','model_seconds','presolve_seconds','lp_iterations','lp_solves','nodes','nlp_iterations','nlp_solves','nlp_seconds','cost','emission','dual_bound','gap','max_violation']
        writer=csv.DictWriter(f,fieldnames=keys);writer.writeheader()
        for record in records:
            for s in record['steps']:
                nlp=nlp_values(s);row={k:s.get(k) for k in keys};row.update(repeat=record['repeat'],profile=record['profile'],level=record['level'],nlp_iterations=nlp['iterations'],nlp_solves=nlp['solves'],nlp_seconds=nlp['seconds']);writer.writerow(row)
    with (ROOT/'Pareto.csv').open('w',newline='') as f:
        writer=csv.writer(f);writer.writerow(['profile','level','cost','emission','warehouses'])
        for record in records:
            if record['repeat']==1 and record['calls']>1:
                for point in record['frontier']:writer.writerow([record['profile'],record['level'],point['cost'],point['emission'],','.join(map(str,point['warehouses']))])
    trends={}
    for p in [f'P{i}' for i in range(1,9)]:
        a=[next(x for x in rows if (x['profile'],x['level'])==(p,l)) for l in 'LMH']
        trends[p]={k:bool(a[0][k]<a[1][k]<a[2][k]) for k in ['solver_ms_median','total_ms_median','lp_iterations_median','nlp_iterations_median']}
    (ROOT/'observed_trends.json').write_text(json.dumps(trends,indent=2))
    print(json.dumps(rows,indent=2));print('Observed trends',trends)
if __name__=='__main__':main()
