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
    counts = sorted(Counter(hand).values(), reverse=True)
    match counts:
        case [5]:
            return HandType.FIVE_OF_A_KIND
        case [4, 1]:
            return HandType.FOUR_OF_A_KIND
        case [3, 2]:
            return HandType.FULL_HOUSE
        case [3, 1, 1]:
            return HandType.THREE_OF_A_KIND
        case [2, 2, 1]:
            return HandType.TWO_PAIR
        case [2, 1, 1, 1]:
            return HandType.ONE_PAIR
        case [1, 1, 1, 1, 1]:
            return HandType.HIGH_CARD
        case _:
            raise Exception(f"unexpected case {counts}")


LABEL_ORDER = "AKQJT98765432"


def solve(data: str):
    hands = [line.split() for line in data.splitlines()]  # (hand, bid)

    def get_sort_key(hand):
        return (classify(hand), tuple(map(LABEL_ORDER.index, hand)))

    hands.sort(key=lambda item: get_sort_key(item[0]), reverse=True)
    total_winnings = 0
    for i, (_hand, bid) in enumerate(hands):
        total_winnings += int(bid) * (i + 1)
    return total_winnings
