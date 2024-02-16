# Assignment

`digit_sum` computes the sum of all the decimal digits of a given number `n`.
For example, `digit_sum(159)` returns `15` because 1+5+9=15.

Start off with a function `last_digit` that returns the last digit of a number.
For example, `last_digit(491)` should return `1`.
Hint: modulo.

Next, write a function `remove_last_digit` that cuts off a number's last digit.
`remove_last_digit(1481)` should return `148`.
Hint: integer division.

Finally, use these two functions to implement `digit_sum`.
