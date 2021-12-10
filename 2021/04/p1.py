import itertools


import itertools


def lmap(f, it):
    return list(map(f, it))


def ints(it):
    return lmap(int, it)


def solve(input):
    M = 10 ** 9

    parts = input.split("\n\n")
    xs = ints(parts[0].split(","))
    boards = [
        [ints(lines[i].split()) for i in range(5)]
        for lines in map(lambda p: p.split("\n"), parts[1:])
    ]

    for x in xs:
        for b in boards:
            for i, j in itertools.product(range(5), repeat=2):
                if b[i][j] == x:
                    b[i][j] = M
            good = any(row.count(M) == 5 for row in b) or any(
                col.count(M) == 5 for col in zip(*b)
            )
            if good:
                return sum(v for v in itertools.chain(*b) if v != M) * x
