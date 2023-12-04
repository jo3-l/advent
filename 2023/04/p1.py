import re


def solve(data: str):
    ans = 0
    for line in data.splitlines():
        m = re.match(r"Card\s+(\d+): (.+?) \| (.+)", line)
        assert m

        winning_numbers = set(map(int, m.group(2).split()))
        selected_numbers = set(map(int, m.group(3).split()))
        wins = len(selected_numbers & winning_numbers)
        if wins > 0:
            ans += 2 ** (wins - 1)
    return ans
