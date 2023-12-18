# Day 3 (2023)

`Gear Ratios` ([prompt](https://adventofcode.com/2023/day/3))

Use this space for notes on the day's solution and to document what you've learned!

## Part 1
- used regex function `finditer()` to find and store numbers
- checked for adjacent symbols by first making a list of all adjacent characters, 
then checking whether any of them are symbols
- used regex match object properties `.start()`, `.end()`, and `.group()` to access
index and value of each found number

## Part 2
- made dictionary containing all gears stored as match objects
- used `find_part_nums()` function from part 1 to compare all gears to the locations
of part numbers
