"""Run all eight profiles with reproducible data and separately measured solver work."""
from argparse import ArgumentParser
from itertools import permutations
import json
from pathlib import Path
from random import Random
from statistics import median
from time import perf_counter

from inti_solver import PROFILES, SolverWork, one_thread_milp
from solver import PAKET_FINAL, SOURCE, ParetoMILP, assemble, buat_paket, jalankan

def benchmark(template, seed, profile, repeats):
    stoch,_,_=PROFILES[profile]
    data,dem=buat_paket(template,seed)
    levels='LMH'
    models={level:assemble(data,dem,level,stoch) for level in levels}
    measured={}
    for level,model in models.items():
        work=SolverWork()
        log=ParetoMILP(work)
        points,frontier=jalankan(data,model,profile,log)
        assert len(work.iterations)==log.calls
        measured[level]=dict(seed=seed,profile=profile,level=level,solver=work.version,
              lp=sum(work.iterations),nodes=log.nodes,calls=log.calls,retries=log.retries,
              points=points,frontier=frontier,times=[])
    orders=list(permutations(levels)) if repeats==6 else [levels[i:]+levels[:i] for i in range(3)]
    Random(seed*31+int(profile[1:])).shuffle(orders)
    for order in orders:
        for level in order:
            log=ParetoMILP(one_thread_milp)
            start=perf_counter()
            points,_=jalankan(data,models[level],profile,log)
            elapsed=1e3*(perf_counter()-start)
            expected=measured[level]
            assert log.calls==expected['calls']
            assert all(abs(p['cost']-q['cost'])<1e-6 and abs(p['emission']-q['emission'])<1e-6
                       for p,q in zip(points,expected['points']))
            expected['times'].append(elapsed)
    for row in measured.values():row['median_ms']=median(row['times'])
    return list(measured.values())

def main():
    parser=ArgumentParser(description=__doc__)
    parser.add_argument('--paket',nargs='+',type=int,default=PAKET_FINAL)
    parser.add_argument('--profil',nargs='+',choices=PROFILES,default=list(PROFILES))
    parser.add_argument('--ulangan',type=int,choices=(3,6),default=3)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    data=json.loads(SOURCE.read_text())
    args.output.parent.mkdir(parents=True,exist_ok=True)
    jobs=[(seed,p) for seed in args.paket for p in args.profil]
    Random(241).shuffle(jobs)
    finished=set()
    if args.output.exists():
        previous={}
        for line in args.output.read_text().splitlines():
            row=json.loads(line)
            previous.setdefault((row['seed'],row['profile']),set()).add(row['level'])
        if any(levels!=set('LMH') for levels in previous.values()):
            raise ValueError('Keluaran terdahulu berisi kombinasi yang belum lengkap.')
        finished=set(previous)
    errors=[]
    with args.output.open('a',encoding='utf-8') as f:
        for seed,p in jobs:
            if (seed,p) in finished:continue
            try:
                rows=benchmark(data,seed,p,args.ulangan)
            except Exception as exc:
                print(f'Gagal paket {seed}, profil {p}: {exc}',flush=True)
                errors.append((seed,p,str(exc)))
                continue
            f.write(''.join(json.dumps(row)+'\n' for row in rows))
            f.flush()
            print(seed,p,[round(r['median_ms'],1) for r in rows],[r['lp'] for r in rows],flush=True)
    if errors:raise RuntimeError(f'{len(errors)} kombinasi gagal: {errors}')

if __name__=='__main__':
    main()
