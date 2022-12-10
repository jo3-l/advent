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


def split_into_groups(rucksacks: list[str], *, size: int):
    return (rucksacks[i * size : (i + 1) * size] for i in range(len(rucksacks) // size))


def solve(data: str):
    ans = 0
    for group in split_into_groups(data.splitlines(), size=3):
        common = as_bitset(group[0])
        for rucksack in group[1:]:
            common &= as_bitset(rucksack)
        ans += common.bit_length() - 1
    return ans
