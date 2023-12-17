# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/2

from ...base import StrSplitSolution, answer
import re


def count_cubes(line) -> int:
    cubes = dict(red = 0, green = 0, blue = 0)

    line = re.sub(",|;", "", line)     
    line = list(line.split(" "))[2:]

    for i in line:
        if i.isdigit():
            count = int(i)
        else:
            cubes[i] = max(count, cubes[i])
    
    return cubes.values()


def check_possible(game, max) -> bool:
    return (game.red <= max[0] 
        and game.green <= max[1]
        and game.blue <= max[2])


class Game:
    """a class used to hold the highest amount of red, green, and blue cubes present in all rounds of one game
    """

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
    
    """returns the power of all max cube counts multiplied together
    """
    def find_power(self) -> int:
        return self.red * self.green * self.blue


class Solution(StrSplitSolution):
    _year = 2023
    _day = 2

    @answer((2416, 63307))
    def solve(self) -> tuple[int, int]:

        # leave games[0] blank so indexes match game numbers
        games = [None] 
        # make Game objects for each line
        for line in self.input:
            games.append(Game(*count_cubes(line)))

        valid_games = []
        max = [12, 13, 14]
        powers = []

        for index, game in enumerate(games[1:], 1):
            if check_possible(game, max):
                valid_games.append(index)
            powers.append(game.find_power())

        return (sum(valid_games), sum(powers))