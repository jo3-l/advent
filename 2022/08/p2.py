from collections.abc import Iterator
from typing import Tuple


def solve(data: str):
    grid = [list(map(int, line)) for line in data.splitlines()]
    rows, cols = len(grid), len(grid[0])
    scenic_scores = [[1] * cols for _ in range(rows)]

    def scan(trees: Iterator[Tuple[int, int]]):
        init_r, init_c = next(trees)
        monostack = [(init_r, init_c)]  # invariant: trees are decreasing in height
        scenic_scores[init_r][init_c] = 0
        for r, c in trees:
            # find closest tree blocking view, if any
            while monostack:
                cand_r, cand_c = monostack[-1]
                if grid[cand_r][cand_c] >= grid[r][c]:
                    break
                monostack.pop()

            if monostack:
                # farthest tree we can see
                blocking_r, blocking_c = monostack[-1]
                scenic_scores[r][c] *= abs(r - blocking_r) + abs(c - blocking_c)
            else:
                # nothing blocking our view
                scenic_scores[r][c] *= abs(r - init_r) + abs(c - init_c)
            monostack.append((r, c))

    for r in range(rows):
        scan((r, c) for c in range(cols))  # left to right
    for r in range(rows - 1, -1, -1):
        scan((r, c) for c in range(cols - 1, -1, -1))  # right to left
    for c in range(cols):
        scan((r, c) for r in range(rows))  # top to bottom
    for c in range(cols - 1, -1, -1):
        scan((r, c) for r in range(rows - 1, -1, -1))  # bottom to top
    return max(max(row) for row in scenic_scores)
