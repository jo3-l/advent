from dataclasses import dataclass


@dataclass
class SectionRange:
    lo: int
    hi: int

    @staticmethod
    def parse(s: str):
        lo, hi = map(int, s.split("-"))
        return SectionRange(lo, hi)


def solve(data):
    ans = 0
    for line in data.splitlines():
        a, b = map(SectionRange.parse, line.split(","))
        if min(a.hi, b.hi) >= max(a.lo, b.lo):
            ans += 1
    return ans
