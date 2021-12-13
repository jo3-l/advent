def lmap(f, it):
    return list(map(f, it))


def ints(it):
    return lmap(int, it)


def solve(input):
    paras = input.split("\n\n")
    points = {tuple(ints(l.split(","))) for l in paras[0].split("\n")}
    typ, z = paras[1].split("\n")[0][len("fold along ") :].split("=")
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
    return len(nxt)
