from collections import Counter


def solve(input):
    paras = input.split("\n\n")
    tmpl = paras[0]
    insert = dict(map(lambda line: line.split(" -> "), paras[1].split("\n")))

    pairs = Counter()
    for a, b in zip(tmpl, tmpl[1:]):
        pairs[a + b] += 1

    first, last = tmpl[0:2], tmpl[-2:]
    for _ in range(10):
        nxt_pairs = Counter()
        for (a, c), n in pairs.items():
            b = insert[a + c]
            nxt_pairs[a + b] += n
            nxt_pairs[b + c] += n
        first = first[0] + insert[first]
        last = insert[last] + last[1]
        pairs = nxt_pairs

    ctr = Counter()
    for p, n in pairs.items():
        ctr[p[0]] += n
        ctr[p[1]] += n

    most, *_, least = ctr.most_common()

    def adjust(e):
        return (e[1] + 1) // 2 if e[0] in (first[0], last[1]) else e[1] // 2

    return adjust(most) - adjust(least)
