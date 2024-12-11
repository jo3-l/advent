from collections import deque

DIRS = ((-1, 0), (0, 1), (1, 0), (0, -1))


def solve(data: str):
    topomap = [list(map(int, line)) for line in data.splitlines()]

    R, C = len(topomap), len(topomap[0])

    def trailhead_score(ti, tj):
        if topomap[ti][tj] != 0:
            return 0

        q = deque([(ti, tj)])
        reachable_peaks = 0
        seen = set()
        while q:
            i, j = q.popleft()
            for dy, dx in DIRS:
                ni, nj = i + dy, j + dx
                if 0 <= ni < R and 0 <= nj < C and (ni, nj) not in seen:
                    if topomap[ni][nj] == topomap[i][j] + 1:
                        seen.add((ni, nj))
                        if topomap[ni][nj] == 9:
                            reachable_peaks += 1
                        else:
                            q.append((ni, nj))
        return reachable_peaks

    ans = 0
    for ti in range(R):
        for tj in range(C):
            ans += trailhead_score(ti, tj)
    return ans
