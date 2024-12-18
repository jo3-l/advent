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
    corrupted: list[tuple[int, int]] = []
    for line in data.splitlines():
        x, y = map(int, line.split(","))
        corrupted.append((x, y))

    lo, hi = 0, len(corrupted) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if not reachable(exit, set(corrupted[:mid])):
            hi = mid
        else:
            lo = mid + 1
    return corrupted[lo - 1]
