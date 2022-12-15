from collections import deque
from dataclasses import dataclass


@dataclass(frozen=True)
class Pos:
    i: int
    j: int

    def iter_adjacent(self):
        for d_i, d_j in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            yield Pos(self.i + d_i, self.j + d_j)


def iter_matches(grid: list[list[str]], elem: str):
    return (
        Pos(i, j)
        for i in range(len(grid))
        for j in range(len(grid[i]))
        if grid[i][j] == elem
    )


def solve(data: str):
    grid = [list(row) for row in data.splitlines()]
    rows, cols = len(grid), len(grid[0])

    src, dst = next(iter_matches(grid, "S")), next(iter_matches(grid, "E"))
    grid[src.i][src.j] = "a"
    grid[dst.i][dst.j] = "z"

    queue = deque(iter_matches(grid, "a"))
    visited = set(queue)
    dist = 0
    while queue:
        n = len(queue)
        for _ in range(n):
            cur = queue.popleft()
            for nxt in cur.iter_adjacent():
                if 0 <= nxt.i < rows and 0 <= nxt.j < cols:
                    if nxt in visited:
                        continue

                    if ord(grid[nxt.i][nxt.j]) <= ord(grid[cur.i][cur.j]) + 1:
                        if nxt == dst:
                            return dist + 1
                        else:
                            visited.add(nxt)
                            queue.append(nxt)
        dist += 1

    return -1
