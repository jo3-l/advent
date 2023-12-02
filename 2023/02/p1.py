from collections import Counter

bag = Counter(red=12, green=13, blue=14)


def solve(data: str):
    total = 0
    for line in data.splitlines():
        game_info, rounds = line.split(": ")
        game_id = int(game_info.removeprefix("Game "))

        good = True
        for round in rounds.split("; "):
            c: Counter[str] = Counter()
            for cube in round.split(", "):
                n, color = cube.split()
                c[color] = int(n)

            if any(c[color] > avail for color, avail in bag.items()):
                good = False
                break

        if good:
            total += game_id

    return total
