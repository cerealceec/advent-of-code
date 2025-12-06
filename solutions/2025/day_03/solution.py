# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/3

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2025
    _day = 3

    def int_list(self, str):
        return [int(x) for x in str]

    @answer(17311)
    def part_1(self) -> int:

        total_jolts = 0

        for bank in self.input:
            batt_1 = max(self.int_list(bank[:-1]))
            batts_remaining = bank[bank.index(str(batt_1)) + 1:]
            batt_2 = max(self.int_list(batts_remaining))
            total_jolts += batt_1*10 + batt_2

        return total_jolts

    @answer(171419245422055)
    def part_2(self) -> int:

        total_jolts = 0

        def find_batt(bank, found) -> str:
            batts_left = 12 - len(found)
            
            if batts_left == 0:
                return ""
            elif len(bank) - batts_left == 0:
                return bank
            else:
                to_search = bank[:len(bank) - batts_left + 1]
                batt = str(max(self.int_list(to_search)))
                batt_index = to_search.index(batt)
                return batt + find_batt(bank[batt_index + 1:], found + batt)

        for bank in self.input:
            total_jolts += int(find_batt(bank, ""))

        return total_jolts
