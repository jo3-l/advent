import re
from dataclasses import dataclass
import math


@dataclass
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


PADDING = "\t" * 5


def display(active: list[list[int]], t: int):
    print(f"t = {t}")
    for row in active:
        print(PADDING + "".join(" " if n == 0 else str(n) for n in row))
    print()


def safety_score(robots_in_quadrant: list[int]):
    return math.prod(robots_in_quadrant[1:])


def solve(data: str, *, width: int, height: int):
    assert width % 2 == 1, "width is not odd"
    assert height % 2 == 1, "height is not odd"

    def quadrant(pos: Vec2):
        x_mid = (width - 1) // 2
        y_mid = (height - 1) // 2
        if pos.y < y_mid:
            if pos.x < x_mid:
                return 1
            elif pos.x > x_mid:
                return 2
        elif pos.y > y_mid:
            if pos.x < x_mid:
                return 3
            elif pos.x > x_mid:
                return 4
        return 0

    active = [[0] * (width + 1) for _ in range(height + 1)]
    robots_in_quadrant = [0] * (4 + 1)

    def add(r: Robot):
        active[r.pos.y][r.pos.x] += 1
        robots_in_quadrant[quadrant(r.pos)] += 1

    def remove(r: Robot):
        active[r.pos.y][r.pos.x] -= 1
        robots_in_quadrant[quadrant(r.pos)] -= 1

    robots = list(map(Robot.parse, data.splitlines()))
    for r in robots:
        add(r)

    t = 0
    score = safety_score(robots_in_quadrant)
    display(active, t)
    while True:
        for r in robots:
            remove(r)
            r.pos += r.velocity
            r.pos.x %= width
            r.pos.y %= height
            add(r)
        t += 1

        new_score = safety_score(robots_in_quadrant)
        if new_score < score * 0.25:
            display(active, t)
            if input("continue? [y/n]") == "n":
                break
        score = new_score
