import itertools
import json
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
    ans = 0
    for i, pair in enumerate(data.split("\n\n")):
        a, b = map(json.loads, pair.splitlines())
        if compare(a, b) <= 0:
            ans += i + 1
    return ans
