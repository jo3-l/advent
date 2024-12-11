from dataclasses import dataclass
from heapq import heappush, heappop
from functools import total_ordering
from typing import Optional


@total_ordering
@dataclass
class Block:
    offset: int
    size: int

    def split(self, left_size: int) -> tuple["Block", "Block"]:
        assert 0 < left_size < self.size
        return Block(self.offset, left_size), Block(
            self.offset + left_size, self.size - left_size
        )

    def __lt__(self, other: "Block"):
        return self.offset < other.offset or (
            self.offset == other.offset and self.size < other.size
        )


@dataclass
class File:
    block: Block
    id: int

    def checksum(self):
        return sum(
            i * self.id
            for i in range(self.block.offset, self.block.offset + self.block.size)
        )


MAX_BLOCK_SIZE = 9


def solve(data: str):
    free_blocks: list[list[Block]] = [[] for _ in range(MAX_BLOCK_SIZE + 1)]
    files: list[File] = []

    cur_id = 0
    cur_offset = 0
    i = 0
    while i < len(data):
        filelen = int(data[i])
        files.append(File(Block(cur_offset, filelen), cur_id))
        cur_offset += filelen
        cur_id += 1
        i += 1

        if i < len(data):
            freelen = int(data[i])
            heappush(free_blocks[freelen], Block(cur_offset, freelen))
            cur_offset += freelen
            i += 1

    for f in reversed(files):
        leftmost: Optional[Block] = None
        for sz in range(f.block.size, MAX_BLOCK_SIZE + 1):
            cands = free_blocks[sz]
            if cands:
                if leftmost:
                    leftmost = min(leftmost, cands[0])
                else:
                    leftmost = cands[0]

        if leftmost and leftmost < f.block:
            heappop(free_blocks[leftmost.size])
            if leftmost.size > f.block.size:  # not a perfect fit
                fit, leftover = leftmost.split(f.block.size)
                f.block = fit
                heappush(free_blocks[leftover.size], leftover)
            else:
                f.block = leftmost

    return sum(f.checksum() for f in files)
