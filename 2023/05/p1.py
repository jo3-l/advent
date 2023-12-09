import re
from dataclasses import dataclass


@dataclass
class MappedRange:
    start: int
    end: int  # exclusive
    offset: int

    def map(self, n: int):
        if self.start <= n < self.end:
            return n + self.offset
        else:
            return n


def extract_ints(s: str):
    return map(int, re.findall(r"\d+", s))


class Mapping:
    mappings: list[MappedRange]

    def __init__(self, mappings: list[MappedRange]):
        self.mappings = mappings

    def map(self, n: int):
        for m in self.mappings:
            mapped = m.map(n)
            if mapped != n:
                return mapped
        return n

    @staticmethod
    def parse(s: str):
        mappings: list[MappedRange] = []
        for line in s.splitlines()[1:]:  # skip header
            dst_start, src_start, range_len = extract_ints(line)
            mappings.append(
                MappedRange(
                    start=src_start,
                    end=src_start + range_len,
                    offset=dst_start - src_start,
                )
            )
        return Mapping(mappings)


def solve(data: str):
    seed_data, *mapping_data = data.split("\n\n")
    (
        seed_to_soil,
        soil_to_fertilizer,
        fertilizer_to_water,
        water_to_light,
        light_to_temp,
        temp_to_humidity,
        humidity_to_loc,
    ) = map(Mapping.parse, mapping_data)

    lowest_loc = float("inf")
    for seed in extract_ints(seed_data):
        soil = seed_to_soil.map(seed)
        fertilizer = soil_to_fertilizer.map(soil)
        water = fertilizer_to_water.map(fertilizer)
        light = water_to_light.map(water)
        temp = light_to_temp.map(light)
        humidity = temp_to_humidity.map(temp)
        loc = humidity_to_loc.map(humidity)

        lowest_loc = min(lowest_loc, loc)
    return lowest_loc
