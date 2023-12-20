# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/4

from ast import Num
from hmac import compare_digest
import numbers
from ...base import StrSplitSolution, answer


def win_nums(line) -> list[int]:
    """return list of winning numbers in card"""
    separator = line.find("|")
    win_list = line[8:separator].split()
    num_list = line[separator+2:].split()
    win_nums = [num for num in num_list if num in win_list]

    return win_nums


class Card:
    def __init__(self, num, win):
        self.num = num
        self.win = win
        self.copies = 1


class Solution(StrSplitSolution):
    _year = 2023
    _day = 4

    @answer(23028)
    def part_1(self) -> int:
        points = 0

        for line in self.input:
            win = win_nums(line)
            points += pow(2, len(win)-1) if len(win) > 0 else 0

        return points

    @answer(9236992)
    def part_2(self) -> int:
        count = 0
        cards_dict = {}

        for index, line in enumerate(self.input, 1):
            cards_dict[index] = Card(index, win_nums(line))
        
        for card in cards_dict.values():
            count += card.copies
            for index, _ in enumerate(card.win, 1):
                cards_dict[card.num + index].copies += card.copies
        
        return count