import math
import re
from collections import defaultdict
from dataclasses import dataclass
from typing import Tuple, Iterator, DefaultDict


@dataclass(frozen=True)
class PartNumber:
    val: int

    row: int
    start_col: int
    end_col: int  # exclusive


def iter_part_numbers(matrix: list[str]) -> Iterator[PartNumber]:
    for i, line in enumerate(matrix):
        for m in re.finditer(r"\d+", line):
            yield PartNumber(
                val=int(m.group(0)), row=i, start_col=m.start(), end_col=m.end()
            )


adj8 = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1, 1), (-1, -1))


def iter_adjacent(r: int, c: int, bounds: Tuple[int, int]) -> Iterator[Tuple[int, int]]:
    for d_r, d_c in adj8:
        n_r = r + d_r
        n_c = c + d_c
        if 0 <= n_r < bounds[0] and 0 <= n_c < bounds[1]:
            yield (n_r, n_c)


GEAR = "*"


def solve(data: str):
    lines = data.splitlines()
    bounds = (len(lines), len(lines[0]))

    # adjacent_parts[i, j] stores IDs of parts adjacent to (i, j)
    adjacent_parts: DefaultDict[Tuple[int, int], set[int]] = defaultdict(set)
    parts = list(iter_part_numbers(lines))
    for part_id, part in enumerate(parts):
        for c in range(part.start_col, part.end_col):
            for adj_r, adj_c in iter_adjacent(part.row, c, bounds):
                adjacent_parts[adj_r, adj_c].add(part_id)

    ans = 0
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if lines[r][c] == GEAR:
                part_ids = adjacent_parts[r, c]
                if len(part_ids) == 2:
                    ans += math.prod(parts[part_id].val for part_id in part_ids)

    return ans
