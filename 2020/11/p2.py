def next_state(cur):
    m, n = len(cur), len(cur[0])
    nxt = [row[:] for row in cur]
    for i in range(m):
        for j in range(n):
            cnt = 0
            for dx, dy in (
                (0, 1),
                (0, -1),
                (1, 0),
                (-1, 0),
                (1, -1),
                (1, 1),
                (-1, -1),
                (-1, 1),
            ):
                n_i, n_j = i + dy, j + dx
                while 0 <= n_i < m and 0 <= n_j < n and cur[n_i][n_j] == ".":
                    n_i += dy
                    n_j += dx
                if 0 <= n_i < m and 0 <= n_j < n and cur[n_i][n_j] == "#":
                    cnt += 1
            if cur[i][j] == "L" and cnt == 0:
                nxt[i][j] = "#"
            elif cur[i][j] == "#" and cnt >= 5:
                nxt[i][j] = "L"
    return nxt


def solve(input):
    state = list(map(list, input.split("\n")))
    while state != (nxt := next_state(state)):
        state = nxt
    cnt = 0
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == "#":
                cnt += 1
    return cnt
