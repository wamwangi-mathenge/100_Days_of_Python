# Instructions

Write a program that works out whether if a given number is an off or even number.

Even numbers can be divided by 2 with no remainder.

eg. 86 is even because 86 / 2 = 43

43 does not have any decimal places. Therefore the division is clean.

eg. 59 is odd because 59 / 2 = 29.5

29.5 is not a whole number, it has decimal places. Therefore there is a remainder of 0.5, so the division is not clean.

The `modulo` is written as a percentage sign (%) in Python. It gives you the remainder after a division.

eg. 

6 / 2 = 3 with no remainder

therefore: 6 % 2 = 0

5 / 2 = 2 * 2 + 2, remainder is 1.

therefore: 5 % 2 = 1

14 / 4 = 3 * 4 + 2, remainder is 2

therefore: 14 % 4 = 2

`Warning` your output should match the Example Output format exactly, even the positions of the commas and full stops.

### Example 1 Input
43
### Example 1 Output
This is an odd number.
### Example 2 Input
94
### Example 2 Output
This is an even number.