import itertools
from collections import Counter
from enum import IntEnum, auto


class HandType(IntEnum):
    FIVE_OF_A_KIND = auto()
    FOUR_OF_A_KIND = auto()
    FULL_HOUSE = auto()
    THREE_OF_A_KIND = auto()
    TWO_PAIR = auto()
    ONE_PAIR = auto()
    HIGH_CARD = auto()


def classify(hand: str):
    ctr = Counter(hand)
    if "J" in ctr:
        del ctr["J"]
    counts = sorted(ctr.values(), reverse=True)

    def matches(expected: list[int]):
        return all(
            got <= want
            for got, want in itertools.zip_longest(counts, expected, fillvalue=0)
        )

    if matches([5]):
        return HandType.FIVE_OF_A_KIND
    elif matches([4, 1]):
        return HandType.FOUR_OF_A_KIND
    elif matches([3, 2]):
        return HandType.FULL_HOUSE
    elif matches([3, 1, 1]):
        return HandType.THREE_OF_A_KIND
    elif matches([2, 2, 1]):
        return HandType.TWO_PAIR
    elif matches([2, 1, 1, 1]):
        return HandType.ONE_PAIR
    elif matches([1, 1, 1, 1, 1]):
        return HandType.HIGH_CARD
    else:
        raise Exception(f"unexpected case {counts}")


LABEL_ORDER = "AKQT98765432J"


def solve(data: str):
    hands = [line.split() for line in data.splitlines()]  # (hand, bid)

    def get_sort_key(hand):
        return (classify(hand), tuple(map(LABEL_ORDER.index, hand)))

    hands.sort(key=lambda item: get_sort_key(item[0]), reverse=True)
    total_winnings = 0
    for i, (_hand, bid) in enumerate(hands):
        print(i + 1, _hand)
        total_winnings += int(bid) * (i + 1)
    return total_winnings
