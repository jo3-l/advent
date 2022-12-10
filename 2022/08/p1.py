from collections.abc import Iterator
from typing import Tuple


def solve(data: str):
    grid = [list(map(int, line)) for line in data.splitlines()]
    rows, cols = len(grid), len(grid[0])
    is_visible = [[False] * cols for _ in range(rows)]

    def scan(trees: Iterator[Tuple[int, int]]):
        init_r, init_c = next(trees)
        max_height = grid[init_r][init_c]
        is_visible[init_r][init_c] = True
        for r, c in trees:
            is_visible[r][c] |= grid[r][c] > max_height
            max_height = max(max_height, grid[r][c])

    for r in range(rows):
        scan((r, c) for c in range(cols))  # left to right
    for r in range(rows - 1, -1, -1):
        scan((r, c) for c in range(cols - 1, -1, -1))  # right to left
    for c in range(cols):
        scan((r, c) for r in range(rows))  # top to bottom
    for c in range(cols - 1, -1, -1):
        scan((r, c) for r in range(rows - 1, -1, -1))  # bottom to top
    return sum(sum(row) for row in is_visible)
