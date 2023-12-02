import math
from collections import Counter

bag = Counter(red=12, green=13, blue=14)


def solve(data: str):
    total = 0
    for line in data.splitlines():
        _, rounds = line.split(": ")

        required: Counter[str] = Counter()
        for round in rounds.split("; "):
            for cube in round.split(", "):
                n, color = cube.split()
                required[color] = max(required[color], int(n))
        total += math.prod(required.values())

    return total
