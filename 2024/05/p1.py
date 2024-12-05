from collections import defaultdict


def solve(data: str):
    rules, updates = map(str.splitlines, data.split("\n\n"))

    goes_before = defaultdict(set)
    for rule in rules:
        x, y = map(int, rule.split("|"))
        goes_before[y].add(x)

    ans = 0
    for update in updates:
        pages = list(map(int, update.split(",")))
        pageset = set(pages)
        seen = set()

        good = True
        for p in pages:
            if all(b in seen for b in goes_before[p] if b in pageset):
                seen.add(p)
            else:
                good = False
                break

        if good:
            ans += pages[len(pages) // 2]
    return ans
