import re
import itertools
from dataclasses import dataclass


@dataclass
class Range:  # half-open
    start: int
    end: int

    # returns (before, intersection, after)
    def cut(self, r: "Range"):
        if r.start >= self.end:
            return Range(r.start, r.start), Range(r.start, r.start), r
        elif r.end <= self.start:
            return r, Range(r.end, r.end), Range(r.end, r.end)
        else:
            lo = max(self.start, r.start)
            hi = min(self.end, r.end)
            return Range(r.start, lo), Range(lo, hi), Range(hi, r.end)

    def __len__(self):
        return max(self.end - self.start, 0)

    def __str__(self):
        return f"[{self.start}, {self.end})"


@dataclass
class MappedRange:
    src: Range
    offset: int

    def map_range(self, r: Range):
        before, intersection, after = self.src.cut(r)
        mapped_intersection = Range(
            intersection.start + self.offset, intersection.end + self.offset
        )
        return before, mapped_intersection, after


def extract_ints(s: str):
    return map(int, re.findall(r"\d+", s))


class Mapping:
    mappings: list[MappedRange]

    def __init__(self, ranges: list[MappedRange]):
        self.mappings = sorted(ranges, key=lambda r: r.src.start)

    def map_ranges(self, ranges: list[Range]):
        return list(itertools.chain.from_iterable(self.map_range(r) for r in ranges))

    def map_range(self, range: Range):
        mapped: list[Range] = []

        cur = range
        for m in self.mappings:
            before, middle, after = m.map_range(cur)
            mapped.append(before)
            mapped.append(middle)
            cur = after
        mapped.append(cur)
        return list(filter(None, mapped))  # remove empty ranges

    @staticmethod
    def parse(s: str):
        mappings: list[MappedRange] = []
        for line in s.splitlines()[1:]:  # skip header
            dst_start, src_start, range_len = extract_ints(line)
            mappings.append(
                MappedRange(
                    src=Range(src_start, src_start + range_len),
                    offset=dst_start - src_start,
                )
            )
        return Mapping(mappings)


def solve(data: str):
    seed_data, *mapping_data = data.split("\n\n")
    seeds = list(extract_ints(seed_data))
    seed_ranges = [
        Range(start, start + range_len)
        for start, range_len in zip(seeds[::2], seeds[1::2])
    ]

    (
        seed_to_soil,
        soil_to_fertilizer,
        fertilizer_to_water,
        water_to_light,
        light_to_temp,
        temp_to_humidity,
        humidity_to_loc,
    ) = map(Mapping.parse, mapping_data)

    soil_ranges = seed_to_soil.map_ranges(seed_ranges)
    fertilizer_ranges = soil_to_fertilizer.map_ranges(soil_ranges)
    water_ranges = fertilizer_to_water.map_ranges(fertilizer_ranges)
    light_ranges = water_to_light.map_ranges(water_ranges)
    temp_ranges = light_to_temp.map_ranges(light_ranges)
    humidity_ranges = temp_to_humidity.map_ranges(temp_ranges)
    loc_ranges = humidity_to_loc.map_ranges(humidity_ranges)
    return min(range.start for range in loc_ranges)
