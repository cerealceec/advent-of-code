# Day 2 (2023)

`Cube Conundrum` ([prompt](https://adventofcode.com/2023/day/2))

## Part 1
parsing the text was the most difficult. learned basic regex to remove any instances of semicolons and commas, then used `split()` to separate text into list of numbers and colours. 

compared each max cube count to the given values (red: 12, green: 13, blue: 14) and if none exceeded the values, added the game's index to an array. returned the sum of the array to get answer.

checked [@xavdid's solution](https://advent-of-code.xavd.id/writeups/2023/day/2/) afterwards and looks like i could have gone further with the regex to keep each quantity paired with its corresponding colour. could have also used `all()` to check each cube count instead of first calculating the max.

## Part 2
very simple with all of the max cube values already calculated in part one; just wrote a function to multiply them all together and added those values up at the end
