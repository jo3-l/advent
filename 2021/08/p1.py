def solve(input):
    n = 0
    for l in input.split("\n"):
        _, _, out = l.partition(" | ")
        n += sum(1 for w in out.split() if len(w) in {2, 3, 4, 7})
    return n
