import os
from itertools import product, accumulate

dir_p = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_p, "input.txt"), "r") as f:
    input = f.read()

K = 25


def solve(input):
    xs = list(map(int, input.split()))
    bad_idx = next(
        i + K
        for i, x in enumerate(xs[K:])
        if not any(xs[j] + xs[k] == x for j, k in product(range(i, i + K), repeat=2))
    )
    lo_idx = {}
    acc = list(accumulate(xs[:bad_idx]))
    for i, x in enumerate(acc):
        c = x - xs[bad_idx]
        if c in lo_idx:
            window = xs[lo_idx[c] + 1 : i + 1]
            return min(window) + max(window)
        lo_idx[acc[i - 1] if i > 0 else 0] = i - 1


print(solve(input.rstrip("\n")))
