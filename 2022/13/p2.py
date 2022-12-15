import itertools
import json
from functools import cmp_to_key
from typing import TypeVar, Union

T = TypeVar("T")
RecursiveList = Union[T, list["RecursiveList"]]


def compare(a: RecursiveList[int], b: RecursiveList[int]) -> int:
    match (a, b):
        case int(), int():
            return (a > b) - (a < b)
        case int(), list():
            return compare([a], b)
        case list(), int():
            return compare(a, [b])
        case list(), list():
            for a_elem, b_elem in zip(a, b):
                cmp = compare(a_elem, b_elem)
                if cmp != 0:
                    return cmp
            return compare(len(a), len(b))


def solve(data: str):
    lists = list(map(json.loads, filter(None, data.splitlines())))

    first_div_packet, second_div_packet = [[2]], [[6]]
    lists.append(first_div_packet)
    lists.append(second_div_packet)
    lists.sort(key=cmp_to_key(compare))
    return (lists.index(first_div_packet) + 1) * (lists.index(second_div_packet) + 1)
