from functools import cache

DIRS = ((-1, 0), (0, 1), (1, 0), (0, -1))


def solve(data: str):
    topomap = [list(map(int, line)) for line in data.splitlines()]

    R, C = len(topomap), len(topomap[0])

    @cache
    def count_uphill_trails(i, j):
        if topomap[i][j] == 9:
            return 1

        cnt = 0
        for dy, dx in DIRS:
            ni, nj = i + dy, j + dx
            if 0 <= ni < R and 0 <= nj < C and topomap[ni][nj] == topomap[i][j] + 1:
                cnt += count_uphill_trails(ni, nj)
        return cnt

    ans = 0
    for i in range(R):
        for j in range(C):
            if topomap[i][j] == 0:
                ans += count_uphill_trails(i, j)
    return ans
