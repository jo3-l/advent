import math
import re
from dataclasses import dataclass


@dataclass(frozen=True)
class Vec2:
    x: int
    y: int

    def __mul__(self, k: int) -> "Vec2":
        return Vec2(self.x * k, self.y * k)

    def __add__(self, other: "Vec2") -> "Vec2":
        return Vec2(self.x + other.x, self.y + other.y)


@dataclass
class Robot:
    _RE = re.compile(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)")

    pos: Vec2
    velocity: Vec2

    @staticmethod
    def parse(s: str):
        m = Robot._RE.match(s)
        assert m is not None, "invalid input"
        px, py, vx, vy = map(int, m.groups())
        return Robot(Vec2(px, py), Vec2(vx, vy))


def solve(data: str, *, t: int, width: int, height: int):
    assert width % 2 == 1, "width is not odd"
    assert height % 2 == 1, "height is not odd"

    def quadrant(x: int, y: int):
        x_mid = (width - 1) // 2
        y_mid = (height - 1) // 2
        if y < y_mid:
            if x < x_mid:
                return 1
            elif x > x_mid:
                return 2
        elif y > y_mid:
            if x < x_mid:
                return 3
            elif x > x_mid:
                return 4
        return 0

    robots_in_quadrant = [0 for _ in range(4 + 1)]
    robots = list(map(Robot.parse, data.splitlines()))
    for r in robots:
        pos = r.pos + r.velocity * t
        robots_in_quadrant[quadrant(pos.x % width, pos.y % height)] += 1
    return math.prod(robots_in_quadrant[1:])
