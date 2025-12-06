from collections import namedtuple


def solve1(s: str):
    valid, ids = s.split("\n\n")
    valid_ranges = []
    for line in valid.splitlines():
        start, end = map(int, line.split("-"))
        valid_ranges.append(range(start, end + 1))

    return sum(
        any(i in valid_range for valid_range in valid_ranges)
        for i in map(int, ids.splitlines())
    )


Interval = namedtuple("Interval", ["start", "end"])


def solve2(s: str):
    valid, _ = s.split("\n\n")
    intervals = []
    for line in valid.splitlines():
        start, end = map(int, line.split("-"))
        intervals.append(Interval(start, end + 1))

    intervals.sort()
    ans = 0
    i = 0
    while i < len(intervals):
        merged_start, merged_end = intervals[i]
        i += 1
        while i < len(intervals) and intervals[i].start < merged_end:
            merged_end = max(merged_end, intervals[i].end)
            i += 1
        ans += merged_end - merged_start

    return ans


with open("in.txt") as f:
    print(solve1(f.read()))
with open("in.txt") as f:
    print(solve2(f.read()))
