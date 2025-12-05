# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/1

from operator import truediv
from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2025
    _day = 1

    @answer((1011, 5937))
    def solve(self) -> tuple[int, int]:
        landed_zero = 0
        passed_zero = 0
        dial = 50
        prev_dial = 0

        for i in self.input:
            rev = 0
            num = int(i[1:])
            if i[0] == "L":
                num *= -1
            prev_dial = dial

            if num < -99 or num > 99:       # check for extra revolutions
                rev = int(num / 100)
                passed_zero += abs(rev)

            num -= rev * 100                # subtract extra revolutions
            dial += num

            if dial % 100 == 0:
                landed_zero += 1
            elif (dial < 0 or dial > 99) and prev_dial != 0:
                passed_zero += 1

            dial = dial % 100
            
        return (landed_zero, passed_zero + landed_zero)