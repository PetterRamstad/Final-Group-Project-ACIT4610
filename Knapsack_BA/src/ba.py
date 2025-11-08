import random
from typing import List, Tuple

def repair_knapsack(x: List[int], w: List[int], W: int) -> List[int]:
    total_w = sum(w[i]*x[i] for i in range(len(x)))
    if total_w <= W:
        return x
    idx = [i for i in range(len(x)) if x[i]==1]
    idx.sort(key=lambda i: w[i], reverse=True)
    x = x[:]
    for i in idx:
        if total_w <= W:
            break
        x[i] = 0
        total_w -= w[i]
    return x

def value(x: List[int], v: List[int], w: List[int], W: int) -> int:
    x = repair_knapsack(x, w, W)
    return sum(v[i]*x[i] for i in range(len(x)))

def bees_algorithm(v: List[int], w: List[int], W: int,
                   n: int = 50, nre: int = 3, nrb: int = 7, nep: int = 8, nsp: int = 20,
                   ngh: int = 3, iters: int = 200, seed: int = 0) -> Tuple[List[int], int, list]:
    random.seed(seed)
    m = len(v)
    scouts = [[random.randint(0,1) for _ in range(m)] for _ in range(n)]
    best, best_val = None, -1
    best_curve = []

    for _ in range(iters):
        scores = [(x, value(x, v, w, W)) for x in scouts]
        scores.sort(key=lambda t: t[1], reverse=True)

        if scores[0][1] > best_val:
            best_val = scores[0][1]
            best = scores[0][0]
        best_curve.append(best_val)

        sites = scores[:nrb]
        new = []
        for i, (x, _) in enumerate(sites):
            recruits = nep if i < nre else nsp
            local_best, local_val = x, value(x, v, w, W)
            for _ in range(recruits):
                y = x[:]
                flips = random.randint(1, max(1, ngh))
                for _ in range(flips):
                    j = random.randrange(m)
                    y[j] ^= 1
                val = value(y, v, w, W)
                if val > local_val:
                    local_best, local_val = y, val
            new.append(local_best)
        while len(new) < n:
            new.append([random.randint(0,1) for _ in range(m)])
        scouts = new

    return repair_knapsack(best, w, W), best_val, best_curve
