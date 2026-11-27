from pathlib import Path
from itertools import combinations
import json
import csv
from solver import SOURCE
import numpy as np
from inti_solver import PROFILES, OPERATION_ROWS, network

data = json.loads(SOURCE.read_text())
high = data["level"]["H"]["jalur_masuk"]
ideal_out = [(g,j,p) for g,p in sorted({(g,p) for _,g,p in high}) for j in range(1,7)]

def support(net, scenario):
    start = scenario * OPERATION_ROWS
    rows = list(range(start,start+OPERATION_ROWS))
    rows += [row for row, s, g in net.time_rows if s == scenario]
    return np.asarray(rows), net.linear[rows] != 0

def weight(matrix):
    common = matrix.astype(np.int64) @ matrix.astype(np.int64).T
    linear_algebra = int(np.triu(common,k=1).sum())
    sets = [set(np.flatnonzero(row)) for row in matrix]
    direct = sum(len(a & b) for a,b in combinations(sets,2))
    assert linear_algebra == direct
    return direct

_, reference = support(network(data,high,ideal_out,{},False),0)
ref = weight(reference)
print('Acuan bersama',ref)
records=[]
for level, specification in data["level"].items():
    baseline = None
    for profile,(stochastic,_,nonlinear) in PROFILES.items():
        net = network(data,specification["jalur_masuk"],specification["jalur_keluar"],specification["permintaan_dasar"],stochastic)
        for scenario in range(3 if stochastic else 1):
            indices, m = support(net,scenario)
            if nonlinear:
                enhanced = m.copy()
                for row, s, g in net.time_rows:
                    if s != scenario: continue
                    id_in_view = list(indices).index(row)
                    for i,(ss,gg,_) in enumerate(net.groups):
                        if (s,g) == (ss,gg): enhanced[id_in_view] |= net.aggregation[i]!=0
                assert np.array_equal(m,enhanced)
            normalized = [{net.names[j] if j<4 else net.names[j].rsplit(',',1)[0]+']'
              for j in np.flatnonzero(row)} for row in m]
            if baseline is None: baseline=normalized
            assert normalized==baseline
            numerator = weight(m)
        records.append([profile,level,len(m),numerator,ref,100*numerator/ref])
    print(level,'43 baris',numerator,f'{100*numerator/ref:.6f}%','P1-P8 sama pada masing-masing kondisi')
if __name__=='__main__':
    from argparse import ArgumentParser
    parser=ArgumentParser()
    parser.add_argument('--output',type=Path)
    target=parser.parse_args().output
    if target:
        target.parent.mkdir(parents=True,exist_ok=True)
        with target.open('w',encoding='utf-8',newline='') as out:
            writer=csv.writer(out)
            writer.writerow(('Profil','Tingkat','Baris operasi per kondisi','Bobot','Acuan','WCC persen'))
            writer.writerows(records)
