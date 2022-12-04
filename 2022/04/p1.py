from collections import namedtuple

SectionRange = namedtuple("SectionRange", ["start", "end"])


def parse_assignment(assignment):
    lo, _, hi = assignment.partition("-")
    return SectionRange(int(lo), int(hi))


def solve(data):
    ans = 0
    for line in data.splitlines():
        a, b = map(parse_assignment, line.split(","))
        if (a.start <= b.start and b.end <= a.end) or (
            b.start <= a.start and a.end <= b.end
        ):
            ans += 1
    return ans
