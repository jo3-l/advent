def get_points(s):
    open, close = "([{<", ")]}>"
    points = [3, 57, 1197, 25137]
    stk = []
    for c in s:
        if c in open:
            stk.append(close[open.index(c)])
        elif not stk or stk.pop() != c:
            return points[close.index(c)]
    return 0


def solve(input):
    return sum(get_points(s) for s in input.split())
