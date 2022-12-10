def cmp_priority(item: str):
    if ord("a") <= ord(item) <= ord("z"):
        return ord(item) - ord("a") + 1
    else:
        return ord(item) - ord("A") + 26 + 1


def as_bitset(rucksack: str):
    items = 0
    for item in rucksack:
        items |= 1 << cmp_priority(item)
    return items


def solve(data):
    ans = 0
    for rucksack in data.splitlines():
        sz = len(rucksack) // 2
        left, right = rucksack[:sz], rucksack[sz:]
        ans += (as_bitset(left) & as_bitset(right)).bit_length() - 1
    return ans
