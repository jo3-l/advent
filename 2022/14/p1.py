from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Point:
    x: int
    y: int


def fall_down(pt: Point, blocked: set[Point]):
    for nxt in (
        Point(pt.x, pt.y + 1),
        Point(pt.x - 1, pt.y + 1),
        Point(pt.x + 1, pt.y + 1),
    ):
        if nxt not in blocked:
            return nxt


def iter_points_on_line(start: Point, end: Point):
    if start.x == end.x:
        for y in range(min(start.y, end.y), max(start.y, end.y) + 1):
            yield Point(start.x, y)
    else:
        for x in range(min(start.x, end.x), max(start.x, end.x) + 1):
            yield Point(x, start.y)


def solve(data: str):
    blocked = set()
    max_y = 0
    for line in data.splitlines():
        prev_pt: Optional[Point] = None
        for raw_coords in line.split(" -> "):
            x, y = map(int, raw_coords.split(","))
            pt = Point(x, y)
            if prev_pt:
                blocked.update(iter_points_on_line(prev_pt, pt))

            prev_pt = pt
            max_y = max(max_y, y)

    ans = 0
    while True:
        prev: Optional[Point] = None
        cur = Point(500, 0)
        while cur and cur.y < max_y:
            prev, cur = cur, fall_down(cur, blocked)

        if cur:
            return ans
        else:
            blocked.add(prev)
            ans += 1
