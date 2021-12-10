def lmap(f, it):
    return list(map(f, it))


def ints(it):
    return lmap(int, it)


def solve(input):
    xs = ints(input.split())
    return sum(1 for a, b in zip(xs, xs[1:]) if b > a)
