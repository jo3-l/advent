def lmap(f, it):
    return list(map(f, it))


def ints(it):
    return lmap(int, it)


def solve(input):
    l = len(input.split()[0])
    xs = lmap(lambda x: int(x, 2), input.split())
    a = 0
    for i in range(l):
        cnt = [0, 0]
        for x in xs:
            cnt[(x >> i) & 1] += 1
        if cnt[1] > cnt[0]:
            a |= 1 << i

    return a * (~a & ((1 << l) - 1))
