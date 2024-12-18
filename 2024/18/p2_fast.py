from dataclasses import dataclass

dirs8 = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1, 1), (-1, -1))


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def neighbors(self):
        for dy, dx in dirs8:
            yield Point(self.x + dx, self.y + dy)


class UnionFind:
    def __init__(self, max_x: int, max_y: int):
        self._parent = [
            [Point(x, y) for y in range(max_y + 1)] for x in range(max_x + 1)
        ]
        self._size = [[1] * (max_y + 1) for _ in range(max_x + 1)]

    def join(self, a: Point, b: Point):
        a_rep = self.representative(a)
        b_rep = self.representative(b)
        if a_rep != b_rep:
            if self.size(a_rep) > self.size(b_rep):
                a_rep, b_rep = b_rep, a_rep

            self._parent[b_rep.x][b_rep.y] = a_rep
            self._size[a_rep.x][a_rep.y] += self.size(b_rep)

    def representative(self, pt: Point):
        parent = self._parent[pt.x][pt.y]
        if parent == pt:
            return parent
        else:
            rep = self.representative(parent)
            self._parent[pt.x][pt.y] = rep
            return rep

    def any_connected(self, xs: list[Point], ys: list[Point]):
        x_reps = set(map(self.representative, xs))
        return any(self.representative(y) in x_reps for y in ys)

    def size(self, pt: Point):
        return self._size[pt.x][pt.y]


def solve(data: str, *, exit: Point):
    top_edge = [Point(x, 0) for x in range(1, exit.x + 1)] + [
        Point(exit.x, y) for y in range(1, exit.y)
    ]
    bottom_edge = [Point(0, y) for y in range(1, exit.y + 1)] + [
        Point(x, exit.y) for x in range(1, exit.x)
    ]

    corrupted = set()
    dsu = UnionFind(exit.x, exit.y)
    for line in data.splitlines():
        x, y = map(int, line.split(","))
        new = Point(x, y)
        corrupted.add(new)
        for adj in new.neighbors():
            if adj in corrupted:
                dsu.join(new, adj)

        if dsu.any_connected(top_edge, bottom_edge):
            return x, y
    assert False, "can always get to exit"
