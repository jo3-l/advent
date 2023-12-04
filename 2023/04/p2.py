from functools import cache
import re


def solve(data: str):
    wins = []

    lines = data.splitlines()
    for line in lines:
        m = re.match(r"Card\s+(\d+): (.+?) \| (.+)", line)
        assert m

        winning_numbers = set(map(int, m.group(2).split()))
        selected_numbers = set(map(int, m.group(3).split()))
        wins.append(len(selected_numbers & winning_numbers))

    @cache
    def calc(c):
        if wins[c] == 0:
            return 1
        return sum(calc(c + i) for i in range(1, wins[c] + 1)) + 1

    return sum(calc(c) for c in range(len(lines)))
