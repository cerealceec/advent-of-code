# Day 2 (2025)

`Gift Shop` ([prompt](https://adventofcode.com/2025/day/2))

## Part 1
split each id in half and check if halves match.

## Part 2
for each id, check all possible repeating sequences whose lengths are between one and half the id's length (ex: for 123124125, check if 1, 12, 123, or 1231 repeat). 

both solutions are slow but work. should learn more regex to know how to do this more efficiently.
