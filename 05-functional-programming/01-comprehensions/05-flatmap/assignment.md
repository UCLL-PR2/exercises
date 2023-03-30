# FlatMap

Consider the following list comprehension:

```python
>>> [[(x, y) for x in range(3)] for y in range(3)]
[
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)]
]
```

As you can see, nothing prevents you from using comprehensions within comprehensions.
In the example above, the result is a list of lists of coordinates.
However, what if we didn't want this nested structured, but instead wished for a list of coordinates?

We want to "flatten" the list of lists into a list.
We can achieve this by rewriting the comprehension above as follows:

```python
>>> [(x, y) for x in range(3) for y in range(3)]
[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
```

You can combine as many `if`s and `for`s as you wish in this way.

## Tasks

* Write a function `genres(movies)` that collects all movie genres in a set.
* Write a function `actors(movies)` that collects all movie actors in a set.
* Write a function `repeat_consecutive(xs, n)` that creates a new list where every element from `xs` is repeated `n` times in the following manner:
  `repeat_consecutive([1, 2, 3], 4)` should return `[1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3]`.
* Write a function `repeat_alternating(xs, n)` that creates a new list where every element from `xs` is repeated `n` times in the following manner:
  `repeat_alternating([1, 2, 3], 4)` should return `[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]`.
* Write a function `cards(values, suits)` that returns a set of all cards that can be made using `values` and `suits`.
  For example, `cards([2, 5, 10], ['hearts', 'diamonds'])` should return `{Card(2, 'hearts'), Card(5, 'hearts'), Card(10, 'hearts'), Card(2, 'diamonds'), Card(5, 'diamonds'), Card(10, 'diamonds')}`.
  You should import the `Card` class from `util`.
