def lmap(f, it):
    return list(map(f, it))


def ints(it):
    return lmap(int, it)


def solve(input):
    h_pos = depth = 0
    for inst in input.split("\n"):
        typ, n = inst.split()
        n = int(n)
        if typ == "forward":
            h_pos += n
        elif typ == "down":
            depth += n
        else:
            depth -= n
    return h_pos * depth
