# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/3

from ...base import StrSplitSolution, answer
import re

def find_adj_chars(engine, index, start, end) -> str:
    '''return string containing all adjacent chars'''
    adj = ""
    # if not first line, check prev line
    if index > 0:  
        adj += engine[index-1][start:end]
    # if not last line, check next line
    if index < len(engine)-1:   
        adj += engine[index+1][start:end]
    # always check current line
        adj += engine[index][start] + engine[index][end-1]
    return adj

def find_part_nums(engine) -> dict:
    '''return dictionary matching line indexes with a list of part numbers
    in that index
    '''
    def is_symbol(char) -> bool:
        return not (char.isdigit() or char == ".")

    part_nums_dict = {}

    for index, line in enumerate(engine):
        # search for numbers
        numbers = re.finditer(r"\d+", line)

        # if found, check whether symbol is adjacent
        if numbers:
            part_nums = []  # list for part numbers found in current line
            for num in numbers:
                # find all adjacent characters
                start = num.start()-1 if num.start() > 0 else num.start()
                end = num.end()+1 if num.end() < len(line)-1 else num.end()
                adj = find_adj_chars(engine, index, start, end)

                # add num to part_nums if adjacent to a symbol
                if [char for char in adj if is_symbol(char)]:
                    part_nums.append(num)
                
        part_nums_dict[index] = part_nums

    return part_nums_dict

def find_adj_nums(gear, line, engine, part_nums):
    '''find all part numbers adjacent to gear'''

    def is_adj(num, gear) -> bool:
        '''return True if num and gear are adjacent'''
        start_dist = abs(num.start() - gear.start())
        end_dist = abs((num.end()-1) - (gear.start()))
        return min(start_dist, end_dist) < 2

    adj_nums = []

    # add all adjacent part numbers to list adj_nums
    if line > 0:
        for num in part_nums[line-1]:
            if is_adj(num, gear):
                adj_nums.append(num)
    if line < len(engine)-1:
        for num in part_nums[line+1]:
            if is_adj(num, gear):
                adj_nums.append(num)
    for num in part_nums[line]:
        if num.end() == gear.start() or num.start() == gear.end():
            adj_nums.append(num)
            
    return adj_nums

class Solution(StrSplitSolution):
    _year = 2023
    _day = 3

    @answer(539433)
    def part_1(self) -> int:
        engine = self.input
        sum = 0

        part_nums = find_part_nums(engine)
        
        for entry in part_nums.values():
            for num in entry:
                sum += int(num.group())

        return sum
        
    @answer(75847567)
    def part_2(self) -> int:
        engine = self.input

        # find all part numbers
        part_nums = find_part_nums(engine)
        gears_dict = {}
        gear_ratios = []

        # find all gears
        for index, line in enumerate(engine):
            gears_dict[index] = []
            found = re.finditer(r"\*", line)
            if found:
                gears_dict[index].extend(found)

        # check whether each gear is adjacent to exactly 2 part numbers
        for line in gears_dict:
            for gear in gears_dict[line]:
                adj_nums = find_adj_nums(gear, line, engine, part_nums)
                if len(adj_nums) == 2:
                    num1 = int(adj_nums[0].group())
                    num2 = int(adj_nums[1].group())
                    gear_ratios.append(num1 * num2)
                
        return sum(gear_ratios)