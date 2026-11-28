"""Predeclared demand perturbations, separate from calibration and main benchmark."""
from pathlib import Path
from itertools import product
from random import Random
import json,copy
from scip_solver import run,DATA,ROOT
protocol=json.loads((ROOT/'calibration_protocol.json').read_text());seeds=protocol['heldout_seeds'];repeats=protocol['repetitions_per_heldout_case'];profiles=protocol['heldout_profiles']
variants={}
for seed in seeds:
    d=copy.deepcopy(DATA);rng=Random(seed);mean=d['level']['L']['permintaan_dasar'].copy()
    for p in 'ABC':
        values=[round(mean[f'{j},{p}']+rng.uniform(-.06,.06),2) for j in range(1,6)];values.append(round(10-sum(values),2))
        for j,value in enumerate(values,1):mean[f'{j},{p}']=value
    for spec in d['level'].values():spec['permintaan_dasar']=dict(mean)
    variants[seed]=d;(ROOT/f'validation_data_{seed}.json').write_text(json.dumps(d,indent=2))
out=ROOT/'validation_variants.jsonl';complete=set()
if out.exists():
    for line in out.read_text().splitlines():
        a=json.loads(line);complete.add((a['repeat'],a['variant'],a['profile'],a['level']))
run('P1','L')
for rep in range(1,repeats+1):
    jobs=list(product(seeds,profiles,'LMH'));Random(94171+rep).shuffle(jobs)
    for seed,p,l in jobs:
        if (rep,seed,p,l) in complete:continue
        result=run(p,l,data=variants[seed]);result.update(repeat=rep,variant=seed)
        with out.open('a') as f:print(json.dumps(result),file=f)
        print(rep,seed,p,l,'seconds',round(result['solver_seconds'],5),'LP',result['lp_iterations'],flush=True)
