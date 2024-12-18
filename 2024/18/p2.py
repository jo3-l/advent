from collections import deque

dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))


def reachable(exit: tuple[int, int], corrupted: set[tuple[int, int]]):
    start = (0, 0)
    q: deque[tuple[int, int]] = deque([start])
    visited: set[tuple[int, int]] = set([start])
    while q:
        x, y = q.popleft()
        for dy, dx in dirs:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx <= exit[0]
                and 0 <= ny <= exit[1]
                and (nx, ny) not in corrupted
                and (nx, ny) not in visited
            ):
                if (nx, ny) == exit:
                    return True
                visited.add((nx, ny))
                q.append((nx, ny))
    return False


def solve(data: str, *, exit: tuple[int, int]):
    corrupted = set()
    for line in data.splitlines():
        x, y = map(int, line.split(","))
        corrupted.add((x, y))
        if not reachable(exit, corrupted):
            return (x, y)

    assert False, "can always get to exit"
