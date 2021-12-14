from collections import Counter


def solve(input):
    paras = input.split("\n\n")
    tmpl = paras[0]
    pairs = Counter()
    for a, b in zip(tmpl, tmpl[1:]):
        pairs[a + b] += 1

    insert = {}
    for line in paras[1].split("\n"):
        p, c = line.split(" -> ")
        insert[p] = c

    first, last = tmpl[0:2], tmpl[-2:]
    for _ in range(40):
        nxt_pairs = Counter()
        for p, n in pairs.items():
            if p in insert:
                nxt_pairs[p[0] + insert[p]] += n
                nxt_pairs[insert[p] + p[1]] += n
            else:
                nxt_pairs[p] += n
        if first in insert:
            first = first[0] + insert[first]
        if last in insert:
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
