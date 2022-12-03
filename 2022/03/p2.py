def compute_priority(item):
    if ord("a") <= ord(item) <= ord("z"):
        return ord(item) - ord("a") + 1
    else:
        return ord(item) - ord("A") + 26 + 1


def get_item_set(rucksack):
    items = 0
    for item in rucksack:
        items |= 1 << compute_priority(item)
    return items


def split_into_groups(rucksacks, *, size):
    return (rucksacks[i * size : (i + 1) * size] for i in range(len(rucksacks) // size))


def solve(data):
    ans = 0
    for group in split_into_groups(data.splitlines(), size=3):
        common = get_item_set(group[0])
        for rucksack in group[1:]:
            common &= get_item_set(rucksack)
        ans += common.bit_length() - 1
    return ans
