from collections import namedtuple

SectionRange = namedtuple("SectionRange", ["start", "end"])


def parse_assignment(assignment):
    lo, _, hi = assignment.partition("-")
    return SectionRange(int(lo), int(hi))


def solve(data):
    ans = 0
    for line in data.splitlines():
        a, b = map(parse_assignment, line.split(","))
        if min(a.end, b.end) >= max(a.start, b.start):
            ans += 1
    return ans
