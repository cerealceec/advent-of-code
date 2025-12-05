# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/2

import string
from ...base import StrSplitSolution, answer
from typing import List


class Solution(StrSplitSolution):
    _year = 2025
    _day = 2
    separator = ","


    @answer(38158151648)
    def part_1(self) -> int:
        invalid = 0

        def halve(str) -> List[str]:
            half_len = len(str) // 2
            first = str[:half_len]
            last = str[half_len:]
            return [first, last]

        for i in self.input:
            id_range = i.split("-")
            first, last = [int(i) for i in id_range]
            for j in range(first, last + 1):
                j = str(j)
                if len(j) % 2 == 0:
                    first_half, last_half = halve(j)
                    if first_half == last_half:
                        invalid += int(j)
            
        return invalid


    @answer(45283684555)
    def part_2(self) -> int:
        invalid = 0

        for i in self.input:
            id_range = i.split("-")
            first, last = [int(i) for i in id_range]
            for j in range(first, last + 1):
                j = str(j)
                for k in range(1, len(j) // 2 + 1):
                    seq = j[:k]          
                    if len(j) % k == 0 and j.count(seq) == len(j) / k:
                        invalid += int(j)
                        break
        
        return invalid