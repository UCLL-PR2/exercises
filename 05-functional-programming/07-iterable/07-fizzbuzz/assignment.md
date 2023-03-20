# Fizz Buzz

[Fizz Buzz](https://en.wikipedia.org/wiki/Fizz_buzz) is a classic problem that tends to pop up in interview questions.
The idea is very simple:

* Start with a list of strings representing numbers: `['1', '2', '3', '4', ...]`.
* If the number if divisible by 3, the string should be replaced by `'fizz'`.
* If the number is divisible by 5, replace it by `'buzz'`.
* If the number is divisible by both 3 and 5, it should become `'fizzbuzz'`.

The first few items of this list are therefore `['1', '2', 'fizz', '4', 'buzz', 'fizz', ...]`.

Write a generator function that produces an infinite list that follows the rules set out above.
