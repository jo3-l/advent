import re


def lmap(f, it):
    return list(map(f, it))


def ints(it):
    return lmap(int, it)


def solve(input):
    min_x, max_x = ints(re.search(r"x=(-?\d+)\.\.(-?\d+)", input).groups())
    min_y, max_y = ints(re.search(r"y=(-?\d+)\.\.(-?\d+)", input).groups())
    return min_y * (min_y + 1) // 2
