from collections import namedtuple
import bisect
import sys
from itertools import pairwise, chain

sys.setrecursionlimit(10**9)

Point = namedtuple("Point", ["y", "x"])


def area(a: Point, b: Point):
    return (abs(a.x - b.x) + 1) * (abs(a.y - b.y) + 1)


def solve1(s: str):
    points: list[Point] = []
    for line in s.splitlines():
        x, y = map(int, line.split(","))
        points.append(Point(y, x))

    N = len(points)
    best = 0
    for i in range(N):
        for j in range(i + 1, N):
            best = max(best, area(points[i], points[j]))
    return best


class RectSumQueries:
    def __init__(self, A):
        R, C = len(A), len(A[0])
        S = [[0] * (C + 1) for _ in range(R + 1)]  # 1-indexed
        for r in range(1, R + 1):
            for c in range(1, C + 1):
                S[r][c] = A[r - 1][c - 1] + S[r][c - 1] + S[r - 1][c] - S[r - 1][c - 1]
        self.S = S
        self.A = A  # TODO

    def sum(self, tl: Point, br: Point):
        tl_r, tl_c = tl.y + 1, tl.x + 1  # convert to 1-indexed
        br_r, br_c = br.y + 1, br.x + 1

        S = self.S
        return (
            S[br_r][br_c]
            - S[tl_r - 1][br_c]
            - S[br_r][tl_c - 1]
            + S[tl_r - 1][tl_c - 1]
        )


class CoordCompress:
    def __init__(self, coords):
        self.sorted_coords = sorted(set(coords))

    def map(self, old):
        idx = bisect.bisect(self.sorted_coords, old) - 1
        assert self.sorted_coords[idx] == old
        return idx

    @property
    def max_mapped(self):
        return len(self.sorted_coords) - 1


def between(lo, hi):
    if lo > hi:
        lo, hi = hi, lo
    return range(lo, hi + 1)


def neighbors(r, c):
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == dc == 0:
                continue
            yield (r + dr, c + dc)


# returns whether the floodfill hit the boundary of A
def floodfillnegative(A, r, c):
    R, C = len(A), len(A[0])
    assert A[r][c] == 0
    A[r][c] = -1
    for nr, nc in neighbors(r, c):
        if 0 <= nr < R and 0 <= nc < C:
            if A[nr][nc] == 0:
                outside = floodfillnegative(A, nr, nc)
                if outside:
                    return True
        else:
            return True
    return False


def repaint(A, oldcolor, newcolor):
    R, C = len(A), len(A[0])
    for r in range(R):
        for c in range(C):
            if A[r][c] == oldcolor:
                A[r][c] = newcolor


def solve2(s: str):
    points: list[Point] = []
    for line in s.splitlines():
        x, y = map(int, line.split(","))
        points.append(Point(y, x))

    Y = CoordCompress((pt.y for pt in points))
    X = CoordCompress((pt.x for pt in points))

    def map_pt(p: Point):
        return Point(Y.map(p.y), X.map(p.x))

    A = [[0] * (X.max_mapped + 1) for _ in range(Y.max_mapped + 1)]
    for a, b in pairwise(chain(points, [points[0]])):
        ya, xa = map_pt(a)
        yb, xb = map_pt(b)
        if ya == yb:
            y = ya
            for x in between(xa, xb):
                A[y][x] = 1
        else:
            assert xa == xb
            x = xa
            for y in between(ya, yb):
                A[y][x] = 1

    # color the interior of the region +1
    for r, c in neighbors(*map_pt(points[0])):
        if 0 <= r < len(A) and 0 <= c < len(A[r]) and A[r][c] == 0:
            outside = floodfillnegative(A, r, c)
            if outside:
                repaint(A, -1, 0)  # retry
            else:
                repaint(A, -1, +1)  # done
                break

    rsq = RectSumQueries(A)
    N = len(points)
    best = 0
    for i in range(N):
        for j in range(i + 1, N):
            u, v = map_pt(points[i]), map_pt(points[j])
            tl = Point(min(u.y, v.y), min(u.x, v.x))
            br = Point(max(u.y, v.y), max(u.x, v.x))
            if rsq.sum(tl, br) == area(tl, br):
                best = max(best, area(points[i], points[j]))
    return best
