from collections import namedtuple
import bisect
import sys
from itertools import pairwise, chain

sys.setrecursionlimit(10**9)  # for `floodfill`

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
        topleft_sum = [[0] * (C + 1) for _ in range(R + 1)]  # 1-indexed
        for r in range(1, R + 1):
            for c in range(1, C + 1):
                topleft_sum[r][c] = (
                    A[r - 1][c - 1]
                    + topleft_sum[r][c - 1]
                    + topleft_sum[r - 1][c]
                    - topleft_sum[r - 1][c - 1]
                )
        self.topleft_sum = topleft_sum

    def sum(self, tl: Point, br: Point):
        tl_r, tl_c = tl.y + 1, tl.x + 1  # convert to 1-indexed
        br_r, br_c = br.y + 1, br.x + 1
        return (
            self.topleft_sum[br_r][br_c]
            - self.topleft_sum[tl_r - 1][br_c]
            - self.topleft_sum[br_r][tl_c - 1]
            + self.topleft_sum[tl_r - 1][tl_c - 1]
        )


def compact(xs):
    N = len(xs)
    i, j = 0, 0
    while i < N:
        xs[j] = xs[i]
        j += 1

        start = i
        i += 1
        while i < N and xs[i] == xs[start]:
            i += 1
    del xs[j:]
    return xs


class CoordCompress:
    def __init__(self, coords):
        self.sorted_coords = compact(sorted(coords))

    def map(self, old):
        i = bisect.bisect_left(self.sorted_coords, old)
        assert self.sorted_coords[i] == old
        return i

    @property
    def max(self):
        return len(self.sorted_coords) - 1


def neighbors(r, c):
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == dc == 0:
                continue
            yield (r + dr, c + dc)


def floodfill(A, r, c, oldcolor, newcolor):
    """Returns whether the floodfill hit the boundary of `A`."""
    R, C = len(A), len(A[0])
    assert A[r][c] == oldcolor

    A[r][c] = newcolor
    hit_boundary = False
    for nr, nc in neighbors(r, c):
        if 0 <= nr < R and 0 <= nc < C:
            if A[nr][nc] == oldcolor:
                hit_boundary |= floodfill(A, nr, nc, oldcolor, newcolor)
        else:
            hit_boundary = True
    return hit_boundary


def between(lo, hi):
    if lo > hi:
        lo, hi = hi, lo
    return range(lo, hi + 1)


def solve2(s: str):
    points: list[Point] = []
    for line in s.splitlines():
        x, y = map(int, line.split(","))
        points.append(Point(y, x))

    y_compress = CoordCompress((pt.y for pt in points))
    x_compress = CoordCompress((pt.x for pt in points))

    def compress(p: Point):
        return Point(y_compress.map(p.y), x_compress.map(p.x))

    R = y_compress.max + 1
    C = x_compress.max + 1
    A = [[0] * C for _ in range(R)]
    for a, b in pairwise(chain(points, [points[0]])):
        ya, xa = compress(a)
        yb, xb = compress(b)
        if ya == yb:
            y = ya
            for x in between(xa, xb):
                A[y][x] = 1
        else:
            assert xa == xb
            x = xa
            for y in between(ya, yb):
                A[y][x] = 1

    # Color the interior of the region +1.
    interior_colors = {1}
    next_color = 2
    for r in range(R):
        for c in range(C):
            if A[r][c] == 0:
                color = next_color
                exterior = floodfill(A, r, c, oldcolor=0, newcolor=color)
                if not exterior:
                    interior_colors.add(color)
                next_color += 1

    for r in range(R):
        for c in range(C):
            A[r][c] = A[r][c] in interior_colors

    rsq = RectSumQueries(A)
    N = len(points)
    best = 0
    for i in range(N):
        for j in range(i + 1, N):
            ya, xa = compress(points[i])
            yb, xb = compress(points[j])
            tl = Point(min(ya, yb), min(xa, xb))
            br = Point(max(ya, yb), max(xa, xb))
            if rsq.sum(tl, br) == area(tl, br):
                best = max(best, area(points[i], points[j]))
    return best
