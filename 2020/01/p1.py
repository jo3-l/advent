def solve(input):
    seen = set()
    for x in map(int, input.split()):
        c = 2020 - x
        if c in seen:
            return c * x
        seen.add(x)
