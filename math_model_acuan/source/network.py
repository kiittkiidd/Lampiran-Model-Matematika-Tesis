"""Canonical business formulation for the frozen P1–P8 distribution case."""
from dataclasses import dataclass
from itertools import product
import numpy as np

PROFILES = {'P1': (False, False, False), 'P2': (True, False, False), 'P3': (False, True, False), 'P4': (True, True, False), 'P5': (False, False, True), 'P6': (True, False, True), 'P7': (False, True, True), 'P8': (True, True, True)}
OPERATION_ROWS = 34
HANDLING_ROWS = 4

@dataclass
class Network:
    linear: np.ndarray
    lower: np.ndarray
    upper: np.ndarray
    bounds: np.ndarray
    cost: np.ndarray
    emission: np.ndarray
    aggregation: np.ndarray
    time_rows: list
    names: list
    groups: list
    weights: np.ndarray


def network(data, inbound, outbound, mean, stochastic):
    scenarios = data["P2"]["skenario"] if stochastic else [{"peluang": 1}]
    probabilities = np.array([s["peluang"] for s in scenarios])
    categories = sorted({(g,p) for _,g,p in data["level"]["H"]["jalur_masuk"]})
    orders = list(product(range(1, 7), "ABC"))
    demands = [dict(mean) for _ in probabilities]
    if stochastic:
        for d, s in zip(demands, scenarios):
            for key in d:
                d[key] *= s["pengali"][key.split(",")[1]]
    n_flows = len(inbound) + len(outbound)
    n = 4 + len(scenarios)*n_flows
    handling_start = OPERATION_ROWS*len(scenarios)
    m = handling_start + HANDLING_ROWS*len(scenarios)
    matrix = np.zeros((m, n))
    lower = np.full(m, -np.inf)
    upper = np.zeros(m)
    bounds = np.r_[np.ones(4), np.full(n-4, np.inf)]
    energy = np.r_[data["P3"]["emisi_tetap_gudang"], np.zeros(n-4)]
    cost = np.r_[data["biaya_buka_gudang"], np.zeros(n-4)]
    names = [f"y[{g}]" for g in range(1,5)]
    settings = data["kontrol_profil"]
    groups = {}
    time_rows = []
    for s, (demand, probability) in enumerate(zip(demands, probabilities)):
        offset = s*OPERATION_ROWS
        i0 = 4+s*n_flows
        upper[offset+12:offset+30] = [demand.get(f"{j},{p}", 0) for j,p in orders]
        lower[offset:offset+30] = upper[offset:offset+30]
        for k, (i,g,p) in enumerate(inbound, i0):
            matrix[offset+categories.index((g,p)),k] = 1
            cost[k] = probability * data["tarif_masuk_per_ton"][i-1][g-1]
            energy[k] = probability * data["P3"]["emisi_masuk_per_ton"][i-1][g-1]
            names.append(f"x[{i},{g},{p},{s+1}]")
        for k, (g,j,p) in enumerate(outbound, i0+len(inbound)):
            matrix[offset+categories.index((g,p)),k] = -1
            matrix[offset+12+orders.index((j,p)),k] = 1
            matrix[offset+29+g,k] = 1
            cost[k] = probability * (data["tarif_keluar_per_ton"][g-1][j-1]
                                      + data["tarif_penanganan_per_ton"][g-1]["ABC".index(p)])
            energy[k] = probability * data["P3"]["emisi_keluar_per_ton"][g-1][j-1]
            names.append(f"z[{g},{j},{p},{s+1}]")
            groups.setdefault((s,g,p), []).append(k)
        for g in range(1,5):
            capacity = offset+29+g
            time = handling_start+HANDLING_ROWS*s+g-1
            matrix[time] = matrix[capacity] * settings["waktu_per_ton"]
            matrix[time,g-1] = -settings["waktu_gudang"][g-1]
            matrix[capacity,g-1] = -data["kapasitas_gudang"][g-1]
            time_rows.append((time,s,g))
    aggregation = np.zeros((len(groups),n))
    for i, cols in enumerate(groups.values()):
        aggregation[i,cols] = 1
    weights = np.array([probabilities[s] for s,_,_ in groups])
    return Network(matrix,lower,upper,bounds,cost,energy,aggregation,time_rows,names,list(groups),weights)

