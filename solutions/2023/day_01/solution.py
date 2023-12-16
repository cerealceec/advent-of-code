# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/1

from ...base import StrSplitSolution, answer

DIGITS_TO_WORDS = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}

class Solution(StrSplitSolution):
    _year = 2023
    _day = 1

    @answer(55621)
    def part_1(self) -> int:

        # find first digit in string
        def find_digit(str):
            for i in str:
                if i.isdigit():
                    digit = i
                    break
            return digit

        sum = 0

        for line in self.input:
            digits = find_digit(line) + find_digit(reversed(line))
            sum += int(digits)

        return sum

    @answer(53592)
    def part_2(self) -> int:

        sum = 0

        # find first digit in string
        def find_digit(line):
            for index, char in line:
                if char.isdigit():
                    return [index, int(char)]

        # find first number word in string
        def find_number(line, digit, reverse=False) -> list:
            number = digit
            # check string for number words "one" through "nine"
            for digit in range(1, 10):
                word = DIGITS_TO_WORDS[digit]
                # find first (or last, if reverse) occurence of word
                word_index = line.find(word) if not reverse else line.rfind(word)

                if not reverse:
                    # if found AND index is lowest so far, overwrite number
                    if word_index > -1 and word_index < number[0]:
                        number = [word_index, digit]              
                else:
                    # if found AND index is highest so far, overwrite number
                    if word_index > -1 and word_index > number[0]:
                        number = [word_index, digit]

            return number

        for line in self.input:
            # find first number 
            first_digit = find_digit(enumerate(line))
            first_number = find_number(line, first_digit)

            # find last number
            last_digit = find_digit(reversed(list(enumerate(line))))
            last_number = find_number(line, last_digit, True)

            # concatenate digits and add to sum
            digits = str(first_number[1]) + str(last_number[1])
            sum += int(digits)

        return sum