from collections import defaultdict, Counter, deque
from functools import cache
import math
import re
import itertools
import os
from heapq import heappush, heappop

adj4 = ((0, -1), (0, 1), (1, 0), (-1, 0))
adj8 = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1, 1), (-1, -1))


def lmap(f, it):
    return list(map(f, it))


def ints(txt):
    return lmap(int, txt)


def make_indexer(lst, default=None):
    def get(*indices):
        cur = lst
        for i in indices:
            if 0 <= i < len(cur):
                cur = cur[i]
            else:
                return default
        return cur

    return get


def solve(input):
    LP = -1
    matrix = [lmap(int, r) for r in input.split()]
    get = make_indexer(matrix, 9)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if all(matrix[i][j] < get(i + dy, j + dx) for dy, dx in adj4):
                matrix[i][j] = LP

    def dfs(i, j):
        n = 1
        for dx, dy in adj4:
            if get(i + dy, j + dx) != 9:
                matrix[i + dy][j + dx] = 9
                n += dfs(i + dy, j + dx)
        return n

    xs = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == LP:
                matrix[i][j] = 9
                xs.append(dfs(i, j))
    xs.sort()
    return math.prod(xs[-3:])


cur_dir = os.path.dirname(os.path.realpath(__file__))

print("SAMPLE OUTPUT")
with open(os.path.join(cur_dir, "sample.txt")) as f:
    print(solve(f.read().strip()))

print("---")

print("OUTPUT")
with open(os.path.join(cur_dir, "input.txt")) as f:
    print(solve(f.read().strip()))
