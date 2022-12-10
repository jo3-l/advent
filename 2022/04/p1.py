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
        if (a.lo <= b.lo and b.hi <= a.hi) or (b.lo <= a.lo and a.hi <= b.hi):
            ans += 1
    return ans
