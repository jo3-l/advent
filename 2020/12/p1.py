from collections import defaultdict, Counter, deque
from functools import cache
import math
import re
import itertools
import os

dir_p = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_p, "input.txt"), "r") as f:
    input = f.read()

offsets = ((0, 1), (1, 0), (0, -1), (-1, 0))


def solve(input):
    dir = 1
    x = y = 0
    for i in input.split():
        t, n = i[0], int(i[1:])
        if t in ("N", "E", "S", "W"):
            idx = ("N", "E", "S", "W").index(t)
            x += offsets[idx][0] * n
            y += offsets[idx][1] * n
        elif t == "L":
            dir -= n // 90
            if dir < 0:
                dir += 4
        elif t == "R":
            dir += n // 90
            if dir >= 4:
                dir -= 4
        else:
            x += offsets[dir][0] * n
            y += offsets[dir][1] * n
    return abs(x) + abs(y)


print(solve(input.rstrip("\n")))
