"""Benchmark dan pemeriksaan kelayakan untuk kasus jaringan multiwilayah."""
from argparse import ArgumentParser
from pathlib import Path
from random import Random
from statistics import median
from time import perf_counter
import json

import numpy as np
from scipy.sparse import coo_matrix, csr_matrix, hstack, vstack

from inti_solver import (FEAS, GAP, PROFILES, HANDLING_ROWS, OPERATION_ROWS,
                         SolverWork, one_thread_milp, network, Bounds, LinearConstraint)

TERRITORIES = {"L":1, "M":4, "H":12}
WEIGHTS = (.15,.325,.5,.675,.85)
CALIBRATION = (8001,8002,8003)
TEST = tuple(range(8201,8211))
COST_SCALE = 300.0
EMISSION_SCALE = 150.0

def region_data(template, seed, area):
    """Variasi deterministik antarwilayah, dengan total palet per produk tetap."""
    import copy
    data = copy.deepcopy(template)
    trials = Random(seed*1009+area)
    data["biaya_buka_gudang"] = [round(x*trials.uniform(.95,1.05),3)
                              for x in data["biaya_buka_gudang"]]
    for key in ("tarif_masuk_per_palet","tarif_keluar_per_palet"):
        data[key] = [[round(x*trials.uniform(.97,1.03),3) for x in row] for row in data[key]]
    demand = template["level"]["L"]["permintaan_dasar"].copy()
    for p in "ABC":
        keys = [k for k in demand if k.endswith(","+p)]
        changes = [trials.uniform(-.20,.20) for _ in keys]
        avg = sum(changes)/len(changes)
        for key, offset in zip(keys,changes):
            demand[key] += offset-avg
    return data, demand

def assemble(template, level, seed, area, stoch):
    data, demand = region_data(template,seed,area)
    spec = data["level"][level]
    local = network(data,spec["jalur_masuk"],spec["jalur_keluar"],demand,stoch)
    handling = [
        (row, qi) for row,scenario,warehouse in local.time_rows
        for qi,(q_s,q_g,_) in enumerate(local.groups) if (q_s,q_g)==(scenario,warehouse)
    ]
    return (csr_matrix(local.linear), local.lower, local.upper,
            local.bounds, local.cost, local.emission, csr_matrix(local.aggregation),
            local.weights, np.arange(4), handling)

def regions_in(level):
    flavors = ("L",) + ("M",)*3 + ("H",)*8
    return enumerate(flavors[:TERRITORIES[level]],1)

def wcc(template):
    def supports(net,scenario):
        start=scenario*OPERATION_ROWS
        rows = list(range(start,start+OPERATION_ROWS))
        rows += [t for t,s,_ in net.time_rows if s==scenario]
        return [
          {name if name.startswith("y[") else name.rsplit(",",1)[0]+"]"
           for name, active in zip(net.names,net.linear[r]!=0) if active} for r in rows]
    def weight(rows):
        from collections import Counter
        covers=Counter(var for row in rows for var in row)
        return sum(n*(n-1)//2 for n in covers.values())
    high = template["level"]["H"]["jalur_masuk"]
    reference_routes = [(g,j,p) for g,p in sorted({(g,p) for _,g,p in high}) for j in range(1,7)]
    reference = weight(supports(network(template,high,reference_routes,{},False),0))
    result={}
    for level,count in TERRITORIES.items():
        spec=template["level"][level]
        args=(template,spec["jalur_masuk"],spec["jalur_keluar"],spec["permintaan_dasar"])
        baseline=supports(network(*args,False),0)
        stoch=network(*args,True)
        assert all(supports(stoch,s)==baseline for s in range(3))
        # Check that every flow in a squared handling term already occurs linearly there.
        for row,s,g in stoch.time_rows:
            for idx,(sg,gg,_) in enumerate(stoch.groups):
                if (s,g)==(sg,gg):
                    assert np.all((stoch.aggregation[idx]==0) | (stoch.linear[row]!=0))
        numerator=weight(baseline)
        result[level]=dict(wilayah=count,bobot_tipe_lokal=numerator,acuan_wilayah=reference,
                           total_bobot=count*numerator,persen=100*numerator/reference)
    for level,count in TERRITORIES.items():
        numerator=sum(result[flavor]["bobot_tipe_lokal"] for _,flavor in regions_in(level))
        result[level].update(total_bobot=numerator, persen=100*numerator/(reference*count))
    return result

def run_model(template, model, nonlinear, multi, log):
    original,lower,upper,ub,cost,emission,volume,prob,binary,handling=model
    n=original.shape[1]
    k=len(prob) if nonlinear else 0
    config=template["kontrol_profil"]
    alpha=config["kenaikan_biaya_kuadratik"] if nonlinear else 0.
    beta=config["kenaikan_waktu_kuadratik"] if nonlinear else 0.
    rows=[a for a,b in handling]
    cols=[b for a,b in handling]
    enrich=csr_matrix((np.full(len(rows),beta),(rows,cols)),shape=(len(upper),k)) if nonlinear else csr_matrix((len(upper),0))
    system=hstack([original,enrich],format="csr")
    integer=np.zeros(n+k)
    integer[binary]=1
    bounds=Bounds(np.zeros(n+k),np.r_[ub,np.full(k,np.inf)])
    tangencies=[{0.,4.,8.,12.,16.,20.} for _ in range(k)]
    metrics=[]
    for lam in WEIGHTS if multi else (1.,):
        cw=lam/COST_SCALE if multi else 1.
        ew=(1.-lam)/EMISSION_SCALE if multi else 0.
        target=np.r_[cw*cost+ew*emission,cw*alpha*prob[:k]]
        nodes=calls=0
        for attempt in range(50):
            q_index=np.repeat(np.arange(k),[len(vals) for vals in tangencies])
            pivots=np.array([point for vals in tangencies for point in sorted(vals)])
            if len(q_index):
                rindex=np.arange(len(q_index))
                cuts=hstack([volume[q_index].multiply(2*pivots[:,None]),
                            coo_matrix((-np.ones(len(rindex)),(rindex,q_index)),shape=(len(rindex),k))],
                            format="csr")
                matrix=vstack([system,cuts],format="csr")
                lo=np.r_[lower,np.full(len(pivots),-np.inf)]
                hi=np.r_[upper,pivots*pivots]
            else:
                matrix,lo,hi=system,lower,upper
            res=log(target,integrality=integer,bounds=bounds,
                    constraints=LinearConstraint(matrix,lo,hi),
                    options={"mip_rel_gap":0.,"time_limit":45.})
            if not res.success:
                raise RuntimeError(res.message)
            calls += 1
            nodes += int(res.mip_node_count or 0)
            x=res.x[:n]
            q=volume@x
            square=q*q
            valid=original@x+(enrich@square if k else 0.)
            charge=float(cost@x+alpha*(prob@square))
            carbon=float(emission@x)
            value=cw*charge+ew*carbon
            gap=value-res.mip_dual_bound
            if (np.all(valid>=lower-FEAS) and np.all(valid<=upper+FEAS)
                and np.all(x>=-FEAS) and np.all(x<=ub+FEAS)
                and np.allclose(x[binary],np.rint(x[binary]),atol=FEAS,rtol=0)
                and gap<=GAP*min(cw,cw+ew) and gap>=-FEAS):
                metrics.append(dict(lam=lam,cost=charge,emission=carbon,gap=float(gap),calls=calls,nodes=nodes))
                break
            updated=False
            for qi in np.flatnonzero(square[:k]-res.x[n:]>1e-9):
                v=round(float(q[qi]),10)
                if v not in tangencies[qi]:
                    tangencies[qi].add(v)
                    updated=True
            if not updated:
                raise RuntimeError(f"Relaksasi tidak memenuhi toleransi, lambda={lam}, gap={gap:.6g}.")
        else:
            raise RuntimeError(f"Batas iterasi pendekatan tercapai, lambda={lam}.")
    return metrics

def evaluate(template,seed,profile,repeats):
    stoch,multi,nonlinear = PROFILES[profile]
    models={area:assemble(template,flavor,seed,area,stoch) for area,flavor in regions_in("H")}
    counts, baseline = {}, {}
    seed_version = None
    for area,model in models.items():
        work=SolverWork()
        baseline[area]=run_model(template,model,nonlinear,multi,work)
        assert len(work.iterations)==sum(r["calls"] for r in baseline[area])
        counts[area]=sum(work.iterations)
        seed_version=work.version
    elapsed = {l:[] for l in TERRITORIES}
    order = list(TERRITORIES)
    rng = Random(seed*17+int(profile[1:]))
    for i in range(repeats+1):
        rng.shuffle(order)
        for l in order:
            start=perf_counter()
            for area,_ in regions_in(l):
                result=run_model(template,models[area],nonlinear,multi,one_thread_milp)
                assert all(abs(a["cost"]-b["cost"])<1e-6 and abs(a["emission"]-b["emission"])<1e-6
                           for a,b in zip(baseline[area],result))
            duration = 1000*(perf_counter()-start)
            if i:
                elapsed[l].append(duration)
    outputs=[]
    for l,size in TERRITORIES.items():
        sol=[]
        for index in range(len(WEIGHTS) if multi else 1):
            points=[baseline[a][index] for a,_ in regions_in(l)]
            sol.append(dict(lam=points[0]["lam"],cost=sum(r["cost"] for r in points),
                            emission=sum(r["emission"] for r in points),gap=sum(r["gap"] for r in points),
                            calls=sum(r["calls"] for r in points),nodes=sum(r["nodes"] for r in points)))
        outputs.append(dict(seed=seed,level=l,profile=profile,regions=size,
                            iterations=sum(counts[a] for a,_ in regions_in(l)),
                            nodes=sum(r["nodes"] for r in sol),calls=sum(r["calls"] for r in sol),
                            median_ms=median(elapsed[l]),times_ms=elapsed[l],solutions=sol,highs=seed_version))
    return outputs

def machine():
    import multiprocessing
    import os
    cores=sorted(os.sched_getaffinity(0))
    worker=multiprocessing.current_process()._identity[-1]
    os.sched_setaffinity(0,{cores[(worker-1)%len(cores)]})

def main():
    from concurrent.futures import ProcessPoolExecutor, as_completed
    import os
    a=ArgumentParser()
    a.add_argument("--set",choices=("kalibrasi","uji"),default="uji")
    a.add_argument("--repetisi",type=int,default=3)
    a.add_argument("--pekerja",type=int,default=1)
    a.add_argument("--output",type=Path,required=True)
    a.add_argument("--hanya",choices=list(PROFILES))
    opts=a.parse_args()
    if opts.repetisi<1 or not 1<=opts.pekerja<=len(os.sched_getaffinity(0)):
        a.error("repetisi minimal satu dan pekerja tidak boleh melebihi CPU yang tersedia")
    if opts.pekerja==1:
        os.sched_setaffinity(0,{min(os.sched_getaffinity(0))})
    template=json.loads((Path(__file__).resolve().parents[1]/"case/Data_Bersama.json").read_text())
    seeds=CALIBRATION if opts.set=="kalibrasi" else TEST
    jobs=[(seed,profile) for seed in seeds for profile in PROFILES if opts.hanya in (None,profile)]
    Random(125).shuffle(jobs)
    opts.output.parent.mkdir(parents=True,exist_ok=True)
    print("WCC",wcc(template),flush=True)
    with opts.output.open("w",encoding="utf-8") as file:
        def write(records):
            for row in records:
                file.write(json.dumps(row)+"\n")
            file.flush()
            print(records[0]["seed"],records[0]["profile"],
                  [r["iterations"] for r in records],[round(r["median_ms"],1) for r in records],flush=True)
        if opts.pekerja==1:
            for seed,profile in jobs:
                write(evaluate(template,seed,profile,opts.repetisi))
        else:
            with ProcessPoolExecutor(max_workers=opts.pekerja,initializer=machine) as ex:
                future_jobs={ex.submit(evaluate,template,*job,opts.repetisi):job for job in jobs}
                for job in as_completed(future_jobs):
                    try:
                        write(job.result())
                    except Exception:
                        print("Gagal",future_jobs[job],flush=True)
                        raise

if __name__=="__main__":
    main()
