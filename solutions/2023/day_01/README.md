# Day 1 (2023)

`Trebuchet?!` ([prompt](https://adventofcode.com/2023/day/1))

## Part 1
- for each line, iterate through line until a digit is found, then exit loop
- do the same in reverse using built-in `reversed()` function

## Part 2
- make dictionary matching digits 1–9 to their corresponding number words (`1: "one"`, etc)
- first find first/last digits as we did in part 1, then check if there are any word numbers before then
- can't stop after finding first matching word because the iterator goes through numbers 1 through 9 in order, and the number word smallest in value may not be the one that occurs earliest
- tried replacing all number words with corresponding digits before running the digit-finding functions used in part 1, but found an edge case: some number words overlap with others (for example, "oneight"). decided on another method, but in retrospect could have just modified the replace function to leave first and last letters in place when replacing words, as seen [here](https://advent-of-code.xavd.id/writeups/2023/day/1/)