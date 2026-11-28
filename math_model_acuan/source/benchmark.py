"""Sequential, reproducible SCIP benchmark. Existing completed runs are retained."""
from pathlib import Path
from itertools import product
from random import Random
from time import perf_counter
import json,hashlib,sys
from scip_solver import run,CONFIG,DATA,PROFILES,ROOT

def main():
    data_hash=hashlib.sha256((ROOT/'data.json').read_bytes()).hexdigest()
    assert data_hash==CONFIG['data_sha256']
    output=ROOT/'benchmark_runs.jsonl';completed=set()
    if output.exists():
        for line in output.read_text().splitlines():
            a=json.loads(line);completed.add((a['repeat'],a['profile'],a['level']))
    protocol=dict(config=CONFIG,data_sha256=data_hash,solver_sha256=hashlib.sha256((ROOT/'scip_solver.py').read_bytes()).hexdigest(),network_sha256=hashlib.sha256((ROOT/'network.py').read_bytes()).hexdigest(),warmup='one unreported P1-L run; same machine and process; sequential jobs',timing='SCIP getSolvingTime sum; model construction and total wall time reported separately',iterations='SCIP getNLPIterations: cumulative LP iterations, summed across scalar solves',data_modified_during_benchmark=False)
    path=ROOT/'benchmark_protocol.json'
    if path.exists():assert json.loads(path.read_text())==protocol,'Protocol changed after benchmark started'
    else:path.write_text(json.dumps(protocol,indent=2))
    run('P1','L')
    for repeat in range(1,CONFIG['benchmark_repeats']+1):
        jobs=list(product(PROFILES,'LMH'));Random(CONFIG['benchmark_order_seed']+repeat).shuffle(jobs)
        for profile,level in jobs:
            if (repeat,profile,level) in completed:continue
            print(f'START repeat={repeat} {profile} {level}',flush=True)
            trace=ROOT/'traces';trace.mkdir(exist_ok=True);tracefile=trace/f'{repeat}_{profile}_{level}.jsonl'
            def progress(s):
                with tracefile.open('a') as f:print(json.dumps(s),file=f)
                print(f"STEP repeat={repeat} {profile} {level} {s['step']} {s['goal']} {s['status']} solver={s['solver_seconds']:.5f}s LP={s['lp_iterations']} nodes={s['nodes']}",flush=True)
            try:
                result=run(profile,level,progress=progress);result.update(repeat=repeat)
            except Exception as exc:
                with (ROOT/'failures.jsonl').open('a') as f:print(json.dumps(dict(repeat=repeat,profile=profile,level=level,error=str(exc))),file=f)
                raise
            with output.open('a') as f:print(json.dumps(result),file=f)
            print(f"DONE repeat={repeat} {profile} {level} solver={result['solver_seconds']:.5f}s total={result['total_seconds']:.5f}s LP={result['lp_iterations']} nodes={result['nodes']}",flush=True)
            assert hashlib.sha256((ROOT/'data.json').read_bytes()).hexdigest()==data_hash
if __name__=='__main__':main()
