from collections import deque
from functools import cache


def solve1(s: str):
    grid = s.splitlines()
    R, C = len(grid), len(grid[0])

    visited = set()

    def branches_hit(r, c) -> int:
        if not (0 <= r < R and 0 <= c < C):
            return 0
        if (r, c) in visited:
            return 0

        visited.add((r, c))
        if grid[r][c] == "^":
            return 1 + branches_hit(r + 1, c - 1) + branches_hit(r + 1, c + 1)
        else:
            return branches_hit(r + 1, c)

    s_c = next((c for c in range(C) if grid[0][c] == "S"))
    return branches_hit(0, s_c)


def solve2(s: str):
    grid = s.splitlines()
    R, C = len(grid), len(grid[0])

    @cache
    def new_branches(r, c) -> int:
        if not (0 <= r < R and 0 <= c < C):
            return 0
        if grid[r][c] == "^":
            return 1 + new_branches(r + 1, c - 1) + new_branches(r + 1, c + 1)
        else:
            return new_branches(r + 1, c)

    s_c = next((c for c in range(C) if grid[0][c] == "S"))
    return 1 + new_branches(0, s_c)


def solve2_bfs(s: str):
    grid = s.splitlines()
    R, C = len(grid), len(grid[0])

    waysto = [[0] * C for _ in range(R)]
    q = deque()
    for c in range(C):
        if grid[0][c] == "S":
            q.append((0, c))
            waysto[0][c] = 1

    splits = 0
    while q:
        L = len(q)
        new = set()

        def add(r, c, fromr, fromc):
            if 0 <= r < R and 0 <= c < C:
                if (r, c) not in new:
                    new.add((r, c))
                    q.append((r, c))
                waysto[r][c] += waysto[fromr][fromc]

        for _ in range(L):
            r, c = q.popleft()
            if r + 1 >= R:
                continue

            if grid[r + 1][c] == "^":
                # split
                splits += 1
                add(r + 1, c - 1, r, c)
                add(r + 1, c + 1, r, c)
            else:
                add(r + 1, c, r, c)
    return sum(waysto[R - 1][c] for c in range(C))
