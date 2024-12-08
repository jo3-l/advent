from collections import defaultdict
from dataclasses import dataclass
import math
import itertools


@dataclass(frozen=True)
class Vec2:
    x: int
    y: int

    def __neg__(self) -> "Vec2":
        return Vec2(-self.x, -self.y)

    def __add__(self, other: "Vec2") -> "Vec2":
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vec2") -> "Vec2":
        return Vec2(self.x - other.x, self.y - other.y)


def parse(data: str) -> tuple[list[str], dict[str, list[Vec2]]]:
    map = data.splitlines()
    antennas = defaultdict(list)
    for y, line in enumerate(map):
        for x, c in enumerate(line):
            if c != ".":
                antennas[c].append(Vec2(x, y))
    return map, antennas


def part1(map: list[str], antennas_by_freq: dict[str, list[Vec2]]):
    antinodes = set()
    for _, antennas in antennas_by_freq.items():
        for a, b in itertools.combinations(antennas, r=2):
            pt1 = a + (a - b)
            pt2 = b + (b - a)
            if in_bounds(map, pt1):
                antinodes.add(pt1)
            if in_bounds(map, pt2):
                antinodes.add(pt2)
    return len(antinodes)


def part2(map: list[str], antennas_by_freq: dict[str, list[Vec2]]):
    antinodes = set()
    for _, antennas in antennas_by_freq.items():
        for a, b in itertools.combinations(antennas, r=2):
            step = a - b
            g = math.gcd(step.x, step.y)
            step = Vec2(step.x // g, step.y // g)
            antinodes.update(
                itertools.takewhile(
                    lambda p: in_bounds(map, p), generate_points(a, step)
                )
            )
            antinodes.update(
                itertools.takewhile(
                    lambda p: in_bounds(map, p), generate_points(a, -step)
                )
            )
    return len(antinodes)


def generate_points(start: Vec2, step: Vec2):
    while True:
        yield start
        start += step


def in_bounds(map: list[str], pt: Vec2):
    return 0 <= pt.y < len(map) and 0 <= pt.x < len(map[pt.y])


with open("input.txt") as f:
    map, antennas_by_freq = parse(f.read())
    print(f"part 1: {part1(map, antennas_by_freq)}")
    print(f"part 2: {part2(map, antennas_by_freq)}")
