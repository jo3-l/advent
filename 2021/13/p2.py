def lmap(f, it):
    return list(map(f, it))


def ints(it):
    return lmap(int, it)


def solve(input):
    paras = input.split("\n\n")
    points = {tuple(ints(l.split(","))) for l in paras[0].split("\n")}
    for fold in paras[1].split("\n"):
        typ, z = fold[len("fold along ") :].split("=")
        z = int(z)

        nxt = set()
        if typ == "x":
            for x, y in points:
                if x > z:
                    x -= 2 * (x - z)
                nxt.add((x, y))
        else:
            for x, y in points:
                if y > z:
                    y -= 2 * (y - z)
                nxt.add((x, y))
        points = nxt

    for x in range(0, 8):
        for y in range(0, 50):
            if (y, x) in points:
                print("#", end="")
            else:
                print(" ", end="")
        print()
