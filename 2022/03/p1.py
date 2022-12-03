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


def solve(data):
    ans = 0
    for rucksack in data.splitlines():
        compartment_size = len(rucksack) // 2
        left, right = rucksack[:compartment_size], rucksack[compartment_size:]
        left_items, right_items = get_item_set(left), get_item_set(right)
        ans += (left_items & right_items).bit_length() - 1
    return ans
