import itertools


def solve(input):
    xs = list(map(int, input.split()))
    for i, x in enumerate(xs[25:]):
        if not any(
            xs[j] + xs[k] == x for j, k in itertools.product(range(i, i + 25), repeat=2)
        ):
            return x
