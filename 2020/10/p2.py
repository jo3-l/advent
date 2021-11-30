from collections import defaultdict, Counter, deque
from functools import cache
import math
import re
import itertools
import os

dir_p = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_p, "input.txt"), "r") as f:
    input = f.read()


def solve(input):
    xs = list(map(int, input.split()))
    xs.append(0)
    xs.sort()
    xs.append(xs[-1] + 3)

    dp = [0] * (len(xs) + 1)
    aux = defaultdict(int)
    aux[0] = dp[0] = 1
    for i in range(1, len(xs) + 1):
        dp[i] = sum(aux[xs[i - 1] - d] for d in range(1, 4))
        aux[xs[i - 1]] += dp[i]
    return dp[len(xs)]


print(solve(input.rstrip("\n")))
