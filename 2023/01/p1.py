def solve(data: str):
    total = 0
    for line in data.splitlines():
        digits = [int(c) for c in line if c.isdigit()]
        total += digits[0] * 10 + digits[-1]
    return total
