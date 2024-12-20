dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))


def points_within(*, radius: int, source: tuple[int, int]):
    i, j = source
    for dist in range(1, radius + 1):
        for dy in range(-dist, dist + 1):
            abs_dx = dist - abs(dy)
            if abs_dx == 0:
                yield dist, (i + dy, j)
            else:
                yield dist, (i + dy, j - abs_dx)
                yield dist, (i + dy, j + abs_dx)


def solve(data: str, *, min_savings: int, max_cheat_dur: int):
    racetrack = data.splitlines()

    path: list[tuple[int, int]] = []
    pathset = set()
    for i, row in enumerate(racetrack):
        for j, cheats_by_saved in enumerate(row):
            if cheats_by_saved == "S":
                path.append((i, j))
                pathset.add((i, j))
    while True:
        i, j = path[-1]
        if racetrack[i][j] == "E":
            break

        found_continuation = False
        for dy, dx in dirs:
            ni, nj = i + dy, j + dx
            if racetrack[ni][nj] != "#" and (ni, nj) not in pathset:
                assert not found_continuation, "more than one valid continuation"
                found_continuation = True

                path.append((ni, nj))
                pathset.add((ni, nj))
        assert found_continuation, "could not continue path"

    dist_to_end = {pos: d for d, pos in enumerate(reversed(path))}
    ans = 0
    for start in path:
        for dur, cheat_end in points_within(radius=max_cheat_dur, source=start):
            if cheat_end in pathset:
                orig_dist = dist_to_end[start] - dur
                saved = orig_dist - dist_to_end[cheat_end]
                if saved >= min_savings:
                    ans += 1
    return ans
