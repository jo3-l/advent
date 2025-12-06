from collections import deque


def neighbors(r, c, R, C):
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == dc == 0:
                continue
            rr = r + dr
            cc = c + dc
            if 0 <= rr < R and 0 <= cc < C:
                yield (rr, cc)


def solve1(s: str):
    grid = s.splitlines()
    R, C = len(grid), len(grid[0])
    ans = 0
    for r, row in enumerate(grid):
        for c, v in enumerate(row):
            if v == "@":
                k = sum(grid[nr][nc] == "@" for nr, nc in neighbors(r, c, R, C))
                ans += k < 4
    return ans


def solve2(s: str):
    q = deque([])

    grid = list(map(list, s.splitlines()))
    R, C = len(grid), len(grid[0])
    for r, row in enumerate(grid):
        for c, v in enumerate(row):
            if v == "@":
                q.append((r, c))

    ans = 0
    while q:
        L = len(q)
        candidates = set()
        for _ in range(L):
            r, c = q.popleft()
            if grid[r][c] != "@":
                continue

            k = sum(grid[nr][nc] == "@" for nr, nc in neighbors(r, c, R, C))
            if k < 4:
                grid[r][c] = "."
                ans += 1
                for nr, nc in neighbors(r, c, R, C):
                    if grid[nr][nc] == "@" and (nr, nc) not in candidates:
                        candidates.add((nr, nc))
                        q.append((nr, nc))

    return ans
