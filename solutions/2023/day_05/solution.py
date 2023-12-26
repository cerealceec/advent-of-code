# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/5

from curses import set_escdelay
from re import S
from ...base import TextSolution, answer

def parse_map(section):
    section = section.split("\n")[1:]
    ranges = [[int(n) for n in line.split()] for line in section]
    
    return Map(ranges)

def conv_rng(src, map) -> list[tuple]:
    """returns a list of tuples containing ranges of consecutive 
    destination values for the given source range.
    """

    split_rngs = []

    def split_rng(src, map_rngs):
        map_rng_list = [(r[1], r[1]+r[2]) for r in map_rngs]

        # if no map ranges remaining, return src unchanged
        if not map_rng_list:
            split_rngs.append(src)
            return

        src_min = src[0]
        src_max = src[0] + src[1]
        map_overall_min = map_rng_list[0][0]
        map_overall_max = map_rng_list[-1][1]

        # if src rng is entirely outside map rng. return src unchanged
        if src_max <= map_overall_min or map_overall_max <= src_min:
            split_rngs.append(src)

        # if src rng min is before map rng min, split src rng
        elif src_min < map_overall_min:
            split_rngs.append((src_min, map_overall_min - src_min))
            split_rng((map_overall_min, src_max - map_overall_min), map_rngs)
            
        for i, map_rng in enumerate(map_rng_list):
            map_min = map_rng[0]
            map_max = map_rng[1]
            if src_min >= map_min and src_min < map_max:
                if src_max <= map_max:
                    split_rngs.append(
                        (map.convert(src_min), src_max - src_min)
                    )
                else:
                    # if src min is
                    split_rngs.append(
                        (map.convert(src_min), map_max - src_min)
                    )
                    split_rng((map_max, src_max - map_max), map_rngs[i+1:])
    
    split_rng(src, map.ranges)

    return split_rngs


class Map:
    def __init__(self, ranges):
        self.ranges = sorted(ranges, key=(lambda x: x[1]))
        self.min = self.ranges[0][1]
        self.max = self.ranges[-1][1] + self.ranges[-1][2]

        self.rranges = sorted(ranges, key=(lambda x: x[0]))
        self.rmin = self.rranges[0][0]
        self.rmax = self.rranges[-1][0] + self.rranges[-1][2]
    
    def convert(self, num) -> int:
        for r in self.ranges:
            dest, src, rng = r[0], r[1], r[2]
            if src <= num < src+rng:
                return num + dest - src
        return num
    
    def rconvert(self, num) -> int:
        for r in self.rranges:
            dest, src, rng = r[1], r[0], r[2]
            if src <= num < src+rng:
                return num + dest - src
        return num


class Solution(TextSolution):
    _year = 2023
    _day = 5

    @answer(340994526)
    def part_1(self) -> int:
        alm = self.input.split("\n\n")
        seeds = [int(n) for n in alm[0].split()[1:]]
        maps = [parse_map(section) for section in alm[1:]]
        locations = []

        for s in seeds:
            for _, map in enumerate(maps):
                if map.min <= s < map.max:
                    s = map.convert(s)
            locations.append(s)

        return min(locations)


    @answer(52210644)
    def part_2(self) -> int:
        alm = self.input.split("\n\n")
        maps = [parse_map(section) for section in alm[1:]]

        seed_rngs = [int(n) for n in alm[0].split()[1:]]
        seed_rngs = list(zip(seed_rngs[::2], seed_rngs[1::2]))

        # convert all seeds to a list of soil ranges. 
        new_rngs = seed_rngs
        for map in maps:
            old_rngs = new_rngs
            new_rngs = []
            for rng in old_rngs:
                new_rng = conv_rng(rng, map)
                new_rngs.extend(new_rng)

        return sorted(new_rngs)[0][0]