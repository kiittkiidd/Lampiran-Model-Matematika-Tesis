"""Jalankan dengan Python 3, NumPy, dan SciPy. Keluaran berupa ringkasan JSON."""
from itertools import combinations, product
from csv import DictReader
import json
from pathlib import Path

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, linprog, milp


DATA = json.loads(
    (Path(__file__).resolve().parents[2] / "case" / "Data_Bersama.json").read_text()
)
PRODUCTS = DATA["produk"]
PLANTS = range(1, 7)
WAREHOUSES = range(1, 5)
CUSTOMERS = range(1, 7)
HIGH_IN = DATA["level"]["H"]["jalur_masuk"]
BALANCES = sorted({(g, p) for _, g, p in HIGH_IN})
DEMAND_KEYS = list(product(CUSTOMERS, PRODUCTS))
SCENARIOS = DATA["P2"]["skenario"]
P1_AUDIT = Path(__file__).resolve().parent.parent / "P1" / "Audit_WCC_Pasangan.csv"


def route_matrices(inbound, outbound):
    """Bentuk 39 posisi baris pada urutan R1–R39 yang dipakai P1."""
    flows = [("x", *a) for a in inbound] + [("z", *a) for a in outbound]
    a = np.zeros((39, len(flows)))
    warehouse_coefficient = np.zeros((39, 4))
    for col, (kind, i, j, p) in enumerate(flows):
        if kind == "x":
            a[i - 1, col] = 1
            a[6 + BALANCES.index((j, p)), col] = 1
        else:
            a[6 + BALANCES.index((i, p)), col] = -1
            a[17 + DEMAND_KEYS.index((j, p)), col] = 1
            a[34 + i, col] = 1
    warehouse_coefficient[35:, :] = -np.diag(DATA["kapasitas_gudang"])
    return a, warehouse_coefficient


def rhs(demand):
    values = [demand.get(f"{j},{p}", 0.0) for j, p in DEMAND_KEYS]
    return np.array(DATA["kapasitas_pabrik"] + [0] * 11 + values + [0] * 4, dtype=float)


def operating_costs(inbound, outbound):
    return np.array(
        [DATA["tarif_masuk_per_palet"][i - 1][g - 1] for i, g, _ in inbound]
        + [
            DATA["tarif_keluar_per_palet"][g - 1][j - 1]
            + DATA["tarif_penanganan_per_palet"][g - 1][PRODUCTS.index(p)]
            for g, j, p in outbound
        ]
    )


def enumerate_warehouses(a, gy, costs, demands, probabilities):
    """Enumerasi 16 pola y; selesaikan satu LP arus untuk setiap skenario."""
    choices = {}
    upper = np.r_[0:6, 35:39]
    for opened in product((0, 1), repeat=4):
        scenario_costs = []
        for demand in demands:
            residual = rhs(demand) - gy @ opened
            result = linprog(
                costs, A_ub=a[upper], b_ub=residual[upper],
                A_eq=a[6:35], b_eq=residual[6:35], bounds=(0, None),
                method="highs",
            )
            if result.status == 2:
                break
            if not result.success:
                raise RuntimeError(result.message)
            scenario_costs.append(result.fun)
        if len(scenario_costs) == len(demands):
            opening = float(np.dot(DATA["biaya_buka_gudang"], opened))
            choices[opened] = (
                opening + float(np.dot(probabilities, scenario_costs)),
                opening,
                scenario_costs,
            )
    return choices


def expanded_rows(a, gy, demands):
    """Susun baris skenario dengan satu set y yang dipakai bersama."""
    n = a.shape[1]
    matrix = np.zeros((39 * len(demands), 4 + n * len(demands)))
    row_upper = np.concatenate([rhs(demand) for demand in demands])
    row_lower = row_upper.copy()
    for scenario_index, _ in enumerate(demands):
        start = 39 * scenario_index
        block = slice(start, start + 39)
        flow_cols = slice(4 + scenario_index*n, 4 + (scenario_index+1)*n)
        matrix[block, :4] = gy
        matrix[block, flow_cols] = a
        row_lower[start:start+6] = -np.inf
        row_lower[start+35:start+39] = -np.inf
    return matrix, row_lower, row_upper


def extensive_form(a, gy, costs, demands, probabilities):
    """Selesaikan MILP deterministik ekuivalen."""
    n = len(costs)
    matrix, row_lower, row_upper = expanded_rows(a, gy, demands)
    objective = np.r_[DATA["biaya_buka_gudang"], np.concatenate(
        [probability * costs for probability in probabilities]
    )]
    result = milp(
        objective, integrality=np.r_[np.ones(4), np.zeros(n*len(demands))],
        bounds=Bounds(0, np.r_[np.ones(4), np.full(n*len(demands), np.inf)]),
        constraints=LinearConstraint(matrix, row_lower, row_upper),
        options={"mip_rel_gap": 0},
    )
    if not result.success:
        raise RuntimeError(result.message)
    return result.fun, matrix


def coupling(matrix):
    incidence = (matrix != 0).astype(np.int64)
    weights = incidence @ incidence.T
    upper = np.triu(weights, 1)
    return {
        "bobot": int(upper.sum()),
        "pasangan_positif": int(np.count_nonzero(upper)),
        "baris_aktif": int(np.count_nonzero(incidence.any(axis=1))),
        "baris_acuan": int(incidence.shape[0]),
        "variabel": int(incidence.shape[1]),
        "nnz": int(incidence.sum()),
    }


def serialise_best(choices):
    value = min(record[0] for record in choices.values())
    tied = [y for y, record in choices.items() if np.isclose(record[0], value)]
    chosen = tied[0]
    return chosen, {
        "biaya_objektif": value,
        "pilihan_optimal": [[f"G{g}" for g, take in zip(WAREHOUSES, y) if take] for y in tied],
        "biaya_buka": choices[chosen][1],
        "biaya_operasi": choices[chosen][2],
        "pola_gudang_layak": len(choices),
    }


def compare_p1_pairs(a, gy, inbound, outbound, audit, level):
    names = [f"y[{g}]" for g in WAREHOUSES]
    names.extend(f"x[{i},{g},{p}]" for i, g, p in inbound)
    names.extend(f"z[{g},{j},{p}]" for g, j, p in outbound)
    supports = [{names[col] for col in np.flatnonzero(row)} for row in np.c_[gy, a]]
    pairs = list(combinations(range(len(supports)), 2))
    assert len(audit) == len(pairs)
    for (i, j), item in zip(pairs, audit):
        assert (item["baris_1"], item["baris_2"]) == (f"R{i+1}", f"R{j+1}")
        shared = supports[i] & supports[j]
        expected = set(filter(None, item[f"variabel_bersama_{level}"].split("; ")))
        assert shared == expected and len(shared) == int(item[f"bobot_{level}"])


def run():
    with P1_AUDIT.open(newline="") as file:
        p1_pairs = list(DictReader(file))
    probabilities = [item["peluang"] for item in SCENARIOS]
    target = DATA["P2"]["sasaran_permintaan"]
    sigma = DATA["P2"]["simpangan_baku"]
    assert np.isclose(sum(probabilities), 1)
    reference_outbound = [(g, j, p) for g, p in BALANCES for j in CUSTOMERS]
    ar, gyr = route_matrices(HIGH_IN, reference_outbound)
    reference_full, _, _ = expanded_rows(ar, gyr, [{}] * len(SCENARIOS))
    single_ref = coupling(np.c_[gyr, ar])["bobot"]
    full_ref = coupling(reference_full)["bobot"]
    assert (single_ref, full_ref) == (232, 708)
    results = {}
    for level, spec in DATA["level"].items():
        inbound = spec["jalur_masuk"]
        outbound = spec["jalur_keluar"]
        mean_demand = spec["permintaan_dasar"]
        demands = [
            {**mean_demand, target: mean_demand[target] + sigma * scenario["deviasi_baku"]}
            for scenario in SCENARIOS
        ]
        assert min(demand[target] for demand in demands) >= 0
        assert np.isclose(np.dot(probabilities, [d[target] for d in demands]), mean_demand[target])
        a, gy = route_matrices(inbound, outbound)
        compare_p1_pairs(a, gy, inbound, outbound, p1_pairs, level)
        costs = operating_costs(inbound, outbound)
        det_choices = enumerate_warehouses(a, gy, costs, [mean_demand], [1.0])
        stoch_choices = enumerate_warehouses(a, gy, costs, demands, probabilities)
        y_det, det = serialise_best(det_choices)
        _, stoch = serialise_best(stoch_choices)
        det_value, _ = extensive_form(a, gy, costs, [mean_demand], [1.0])
        stoch_value, expanded = extensive_form(a, gy, costs, demands, probabilities)
        assert np.isclose(det_value, det["biaya_objektif"])
        assert np.isclose(stoch_value, stoch["biaya_objektif"])
        base, full = coupling(np.c_[gy, a]), coupling(expanded)
        assert base["bobot"] == {"L":64,"M":97,"H":187}[level]
        assert full["bobot"] == 3 * base["bobot"] + 12
        block_weights = [
            coupling(expanded[39*s:39*(s+1)])["bobot"] for s in range(3)
        ]
        assert block_weights == [base["bobot"]] * 3
        results[level] = {
            "permintaan_K1_A": [scenario[target] for scenario in demands],
            "P1": det,
            "P2": stoch,
            "biaya_y_P1_dalam_P2": stoch_choices[y_det][0] if y_det in stoch_choices else None,
            "audit_satu_blok": {**base, "penyebut":single_ref, "wcc_persen":100*base["bobot"]/single_ref},
            "audit_penuh": {**full, "penyebut":full_ref, "wcc_persen":100*full["bobot"]/full_ref},
        }
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    run()
