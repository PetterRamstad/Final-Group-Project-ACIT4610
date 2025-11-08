import os
from typing import Tuple, List

def load_instance_burkardt(base_dir: str, name: str) -> Tuple[List[int], List[int], int]:
    inst_dir = os.path.join(base_dir, name)
    with open(os.path.join(inst_dir, f"{name}_c.txt")) as f:
        W = int(f.read().strip())
    with open(os.path.join(inst_dir, f"{name}_w.txt")) as f:
        w = [int(x) for x in f.read().strip().split()]
    with open(os.path.join(inst_dir, f"{name}_p.txt")) as f:
        v = [int(x) for x in f.read().strip().split()]
    assert len(v) == len(w), "weights and profits mismatch"
    return v, w, W
