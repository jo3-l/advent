adj4 = ((0, 1), (1, 0), (0, -1), (-1, 0))


def solve(input):
    dir = 1
    x = y = 0
    for i in input.split():
        t, n = i[0], int(i[1:])
        if t in ("N", "E", "S", "W"):
            idx = ("N", "E", "S", "W").index(t)
            x += adj4[idx][0] * n
            y += adj4[idx][1] * n
        elif t == "L":
            dir -= n // 90
            if dir < 0:
                dir += 4
        elif t == "R":
            dir += n // 90
            if dir >= 4:
                dir -= 4
        else:
            x += adj4[dir][0] * n
            y += adj4[dir][1] * n
    return abs(x) + abs(y)
