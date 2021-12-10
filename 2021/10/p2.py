import statistics


def get_completion_points(s):
    open, close = "([{<", ")]}>"
    stk = []
    for c in s:
        if c in open:
            stk.append(close[open.index(c)])
        elif not stk or stk.pop() != c:
            return 0
    score = 0
    for c in reversed(stk):
        score *= 5
        score += close.index(c) + 1
    return score


def solve(input):
    return statistics.median(
        filter(bool, (get_completion_points(s) for s in input.split()))
    )
