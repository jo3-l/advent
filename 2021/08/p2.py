import itertools


def solve(input):
    good = [
        "abcefg",
        "cf",
        "acdeg",
        "acdfg",
        "bcdf",
        "abdfg",
        "abdefg",
        "acf",
        "abcdefg",
        "abcdfg",
    ]
    n = 0
    for l in input.split("\n"):
        observed, _, out = l.partition(" | ")
        observed = observed.split()
        for conf in itertools.permutations("abcdefg"):
            trans = str.maketrans(dict(zip(conf, "abcdefg")))
            if all("".join(sorted(w.translate(trans))) in good for w in observed):
                n += int(
                    "".join(
                        str(good.index("".join(sorted(w.translate(trans)))))
                        for w in out.split()
                    )
                )
    return n
