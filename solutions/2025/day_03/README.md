# Day 3 (2025)

`Lobby` ([prompt](https://adventofcode.com/2025/day/3))

## Part 1
for each bank, find first digit by finding the max value between first & second-to-last digit (to leave room for the second digit). second digit is max value of all digits to the right of the first digit.

## Part 2
similar to part 1 but implemented recursively, leaving room for the remaining digits. base case is when all 12 digits have been found, or there are exactly enough digits remaining in bank.