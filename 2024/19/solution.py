from functools import cache


class TrieNode:
    def __init__(self):
        self.children: dict[str, "TrieNode"] = {}
        self.leaf = False

    def insert(self, phrase: str):
        cur = self
        for c in phrase:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.leaf = True


def solve(data: str):
    patterns, designs = data.split("\n\n")

    trie = TrieNode()
    for p in patterns.split(", "):
        trie.insert(p)

    @cache
    def ways_to_make(design: str):
        if design == "":
            return 1
        cur = trie
        ways = 0
        for i, c in enumerate(design):
            if c not in cur.children:
                return ways
            cur = cur.children[c]
            if cur.leaf:
                ways += ways_to_make(design[i + 1 :])
        return ways

    ways = list(map(ways_to_make, designs.splitlines()))
    print(f"part 1: {sum(w > 0 for w in ways)}")
    print(f"part 2: {sum(ways)}")
