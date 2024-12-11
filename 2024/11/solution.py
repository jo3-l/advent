from functools import cache


def solve(data: str, blinks: int):
    @cache
    def go(num, steps_remaining):
        if steps_remaining == 0:
            return 1

        if num == 0:
            return go(1, steps_remaining - 1)
        elif len(s := str(num)) % 2 == 0:
            half = len(s) // 2
            return go(int(s[:half]), steps_remaining - 1) + go(
                int(s[half:]), steps_remaining - 1
            )
        else:
            return go(num * 2024, steps_remaining - 1)

    return sum(go(n, blinks) for n in map(int, data.split()))
