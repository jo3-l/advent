def lmap(f, it):
    return list(map(f, it))


def ints(it):
    return lmap(int, it)


def solve(input):
    xs = ints(input.split())
    cnt = 0
    for i in range(len(xs) - 3):
        window = sum(xs[i : i + 3])
        nxt = sum(xs[i + 1 : i + 4])
        if nxt > window:
            cnt += 1
    return cnt
