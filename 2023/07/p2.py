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


WILDCARD = "J"


def classify(hand: str):
    ctr = Counter(hand)
    if WILDCARD in ctr:
        del ctr[WILDCARD]
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

    def sort_key(hand):
        return (classify(hand), tuple(map(LABEL_ORDER.index, hand)))

    hands.sort(key=lambda item: sort_key(item[0]), reverse=True)
    return sum(int(bid) * (i + 1) for i, (hand, bid) in enumerate(hands))
