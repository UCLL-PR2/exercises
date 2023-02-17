# Assignment

Write a function `coins(one, two, five, goal)` that checks whether it is possible to form the target amount `goal` given `one`, `two` and `five` coins of denominations 1, 2 and 5, respectively.

A few examples:

* `coins(1, 1, 1, 6)` should return `True`: we can use the 5-coin and 1-coin to make 6.
* `coins(1, 1, 1, 8)` should return `True`: using all three coins we get makes 8.
* `coins(1, 1, 1, 4)` should return `False`: there is no way to make 4 with 1, 2, and 5.

Hint: use nested loops to go through all possible combinations.
For example, `coins(2, 1, 0)` should check

* 0 &times; one-coin + 0 &times; two-coin + 0 &times; five-coin.
* 1 &times; one-coin + 0 &times; two-coin + 0 &times; five-coin.
* 2 &times; one-coin + 0 &times; two-coin + 0 &times; five-coin.
* 0 &times; one-coin + 1 &times; two-coin + 0 &times; five-coin.
* 1 &times; one-coin + 1 &times; two-coin + 0 &times; five-coin.
* 2 &times; one-coin + 1 &times; two-coin + 0 &times; five-coin.
