from dataclasses import dataclass
import functools
from typing import Union


def lmap(f, it):
    return list(map(f, it))


Node = Union["IntNode", "PairNode"]


@dataclass(repr=False)
class IntNode:
    val: int
    pos: int

    def __repr__(self):
        return str(self.val)


@dataclass(repr=False)
class PairNode:
    left: Node
    right: Node

    def __repr__(self):
        return f"[{self.left},{self.right}]"


def parse(s):
    val = eval(s)
    pos_ctr = 0

    def transform(val):
        nonlocal pos_ctr
        if isinstance(val, int):
            pos = pos_ctr
            pos_ctr += 1
            return IntNode(val, pos)
        else:
            return PairNode(transform(val[0]), transform(val[1]))

    return transform(val)


def split(node: Node):
    if isinstance(node, IntNode):
        if node.val >= 10:
            return (
                PairNode(
                    IntNode(node.val // 2, -1),
                    IntNode(node.val // 2 + (node.val & 1), -1),
                ),
                True,
            )
        return node, False
    left, left_split = split(node.left)
    if left_split:
        return PairNode(left, node.right), True
    right, right_split = split(node.right)
    return PairNode(left, right), right_split


def add_rightmost(node: Node, n: int, pos: int):
    if isinstance(node, IntNode):
        if node.pos < pos:
            return IntNode(node.val + n, node.pos), True
        return node, False
    right, right_added = add_rightmost(node.right, n, pos)
    if right_added:
        return PairNode(node.left, right), True
    left, left_added = add_rightmost(node.left, n, pos)
    return PairNode(left, right), left_added


def add_leftmost(node: Node, n: int, pos: int):
    if isinstance(node, IntNode):
        if node.pos > pos:
            return IntNode(node.val + n, node.pos), True
        return node, False
    left, left_added = add_leftmost(node.left, n, pos)
    if left_added:
        return PairNode(left, node.right), True
    right, right_added = add_leftmost(node.right, n, pos)
    return PairNode(left, right), right_added


def find_explosion_target(node: Node, depth=1):
    if isinstance(node, IntNode):
        return node, None
    elif depth == 5:
        return node, node
    else:
        left, found = find_explosion_target(node.left, depth + 1)
        if found:
            if found is node.left:
                return PairNode(IntNode(0, -1), node.right), found
            return PairNode(left, node.right), found
        right, found = find_explosion_target(node.right, depth + 1)
        if found is node.right:
            return PairNode(left, IntNode(0, -1)), found
        return PairNode(left, right), found


def fix_pos(node: Node):
    pos_ctr = 0

    def fix(node: Node):
        nonlocal pos_ctr
        if isinstance(node, IntNode):
            pos = pos_ctr
            pos_ctr += 1
            return IntNode(node.val, pos)
        else:
            return PairNode(fix(node.left), fix(node.right))

    return fix(node)


def explode(node: Node):
    node, found = find_explosion_target(node)
    node = fix_pos(node)
    if found:
        node, _ = add_rightmost(node, found.left.val, found.left.pos)
        node, _ = add_leftmost(node, found.right.val, found.left.pos)
    return node, found is not None


def reduce1(node: Node):
    node, exploded = explode(node)
    if exploded:
        return fix_pos(node), True
    node, did_split = split(node)
    return fix_pos(node), did_split


def reduce(node: Node):
    reduced = True
    while reduced:
        node, reduced = reduce1(node)
    return node


def add(a: Node, b: Node):
    return reduce(fix_pos(PairNode(a, b)))


def magnitude(node: Node):
    if isinstance(node, IntNode):
        return node.val
    return 3 * magnitude(node.left) + 2 * magnitude(node.right)


def solve(input):
    nodes = lmap(parse, input.split("\n"))
    return magnitude(functools.reduce(nodes, add))
