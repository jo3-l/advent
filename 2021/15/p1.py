from heapq import heappush, heappop
import math

adj4 = ((0, -1), (0, 1), (1, 0), (-1, 0))


def lmap(f, it):
    return list(map(f, it))


def ints(it):
    return lmap(int, it)


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
    matrix = [ints(l) for l in input.split("\n")]
    m, n = len(matrix), len(matrix[0])
    get = make_indexer(matrix, -1)

    heap = []
    heappush(heap, (0, 0, 0))
    best = [[math.inf] * n for _ in range(m)]
    best[0][0] = 0
    while heap:
        rsk, i, j = heappop(heap)
        if best[i][j] != rsk:
            continue
        for dx, dy in adj4:
            if get(i + dy, j + dx) != -1:
                nxt_rsk = rsk + get(i + dy, j + dx)
                if nxt_rsk < best[i + dy][j + dx]:
                    best[i + dy][j + dx] = nxt_rsk
                    heappush(heap, (nxt_rsk, i + dy, j + dx))
    return best[-1][-1]
