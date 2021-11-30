import os
from itertools import product

dir_p = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_p, "input.txt"), "r") as f:
    input = f.read()


def solve(input):
    xs = list(map(int, input.split()))
    for i, x in enumerate(xs[25:]):
        if not any(xs[j] + xs[k] == x for j, k in product(range(i, i + 25), repeat=2)):
            return x


print(solve(input.rstrip("\n")))
