from collections import defaultdict
from functools import cmp_to_key


def solve(data: str):
    rules, updates = map(str.splitlines, data.split("\n\n"))

    goes_before = defaultdict(set)
    for rule in rules:
        x, y = map(int, rule.split("|"))
        goes_before[y].add(x)

    ans = 0
    for update in updates:
        pages = list(map(int, update.split(",")))
        sorted_pages = sorted(
            pages, key=cmp_to_key(lambda x, y: -1 if x in goes_before[y] else 1)
        )
        if pages != sorted_pages:
            ans += sorted_pages[len(sorted_pages) // 2]
    return ans
