"""Public default entry point for the frozen case. SCIP is the only default engine."""
from pathlib import Path
import argparse,hashlib,json
from scip_solver import CONFIG,PROFILES,ROOT,run

def solve_default(profile='P1',level='L',progress=None):
    if profile not in PROFILES or level not in 'LMH' or len(level)!=1:raise ValueError('Choose P1–P8 and L, M, or H.')
    if CONFIG['default_solver']!='SCIP':raise ValueError('The frozen reference requires SCIP.')
    if hashlib.sha256((ROOT/'data.json').read_bytes()).hexdigest()!=CONFIG['data_sha256']:raise ValueError('The case data differ from the frozen version. Re-audit changed data before using this reference.')
    return run(profile,level,progress=progress)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--profile',choices=list(PROFILES),default='P1');parser.add_argument('--level',choices=list('LMH'),default='L');parser.add_argument('--output',type=Path,default=Path('hasil_solusi.json'));args=parser.parse_args()
    def progress(s):print(f"Langkah {s['step']}: {s['goal']}; status {s['status']}; waktu SCIP {s['solver_seconds']:.4f} detik; iterasi LP {s['lp_iterations']}",flush=True)
    result=solve_default(args.profile,args.level,progress=progress);args.output.write_text(json.dumps(result,indent=2))
    print(json.dumps({k:result[k] for k in ['profile','level','cost_min','warehouses','calls','solver_seconds','total_seconds','lp_iterations','nodes','max_violation','max_gap']},indent=2))
