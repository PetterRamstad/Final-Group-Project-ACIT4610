import sys, os, time, csv
import matplotlib.pyplot as plt
sys.path.append(os.path.dirname(__file__))

from src.ba import bees_algorithm
from src.loader_burkardt import load_instance_burkardt

INSTANCES = ["p01","p02","p03","p04","p05","p07"]
SEEDS = list(range(10))
ITERS = 200
BA_PARAMS = dict(n=50, nre=3, nrb=7, nep=8, nsp=20, ngh=3)

def ensure_dirs():
    os.makedirs("out/plots", exist_ok=True)

def run_one(inst, seed):
    v, w, W = load_instance_burkardt("data", inst)
    x, val, curve = bees_algorithm(v, w, W, iters=ITERS, seed=seed, **BA_PARAMS)
    used_w = sum(w[i]*x[i] for i in range(len(x)))
    plt.figure()
    plt.plot(curve)
    plt.xlabel("Iteration"); plt.ylabel("Best value so far")
    plt.title(f"BA Convergence – {inst} (seed={seed})")
    plt.tight_layout()
    fig_path = os.path.join("out", "plots", f"{inst}_seed{seed}.png")
    plt.savefig(fig_path, dpi=150)
    plt.close()
    return {"instance": inst, "n": len(v), "W": W, "best_value": val,
            "used_weight": used_w, "iter_to_best": curve.index(val)+1, "seed": seed}

def main():
    ensure_dirs()
    results = []
    t0 = time.perf_counter()
    for inst in INSTANCES:
        print(f"\n=== Instance {inst} ===")
        for s in SEEDS:
            row = run_one(inst, s)
            results.append(row)
            print(f" seed {s:02d}: best={row['best_value']} used={row['used_weight']}/{row['W']} iter_to_best={row['iter_to_best']}")
    best_by_inst = {}
    for r in results:
        k = r["instance"]
        if k not in best_by_inst or r["best_value"] > best_by_inst[k]["best_value"]:
            best_by_inst[k] = r
    with open(os.path.join("out", "summary.csv"), "w", newline="") as f:
        wr = csv.DictWriter(f, fieldnames=["instance","n","W","best_value","used_weight","iter_to_best","seed"])
        wr.writeheader()
        for k in INSTANCES:
            wr.writerow(best_by_inst[k])
    dt = time.perf_counter() - t0
    print(f"\nSaved: out/summary.csv")
    print(f"All done in {dt:.2f}s. Plots in out/plots/*.png")

if __name__ == "__main__":
    main()
