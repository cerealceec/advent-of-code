# Day 5 (2023)

`If You Give A Seed A Fertilizer` ([prompt](https://adventofcode.com/2023/day/5))

## Part 1

- map key: destination range start, source range start, range length

- example: 
    seed-to-soil:
        50 98 2
            - destination range start 50, source range start 98, range length 2
            - source range starts at 98 and has 2 values, 98 and 99
            - destination range starts at 50 and also has 2 values, so 50 and 51
            - so, seed 50 corresponds to soil 98, and seed 51 to soil 99
        52 50 48
            - source: 50, 51, ..., 96, 97
            - destination: 52, 53, ..., 98, 99
            - seed 53 -> soil 55

- tried making a dictionary for each map, but with the values in the input, it's not feasible to store every single key and value. will have to use functions to calculate keys and values instead
- made a Map class to store each map, including a function that converts numbers from source to destination

## Part 2

- can't iterate over a zip() twice??
- efficiency.... uh oh
- brute forced it in 783.4 seconds by doing the search backwards (iterating over all possible location numbers one by one starting from 0, stopping when the corresponding seed number matches one of the given seed numbers)
- did a complete rehaul of part 2 to get it to run faster. function `conv_rng()` now converts any source range into corresponding destination range, split into multiple ranges if necessary. runs in ~5 ms. WHEW
