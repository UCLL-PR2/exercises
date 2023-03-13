# Generator Expressions

Previously, we discussed three kinds of comprehensions:

* List comprehensions: `[expr for x in xs]`.
* Set comprehensions: `{expr for x in xs}`.
* Dictionary comprehensions: `{key: value for x in xs}`.

There's one more kind of comprehension, namely the _generator expression_.
Its syntax is `(expr for x in xs)` and it produces the same items as `[expr for x in xs]`, except for the fact that instead of computing all elements immediately and storing them in memory, the generator expression returns an iterator that will produce the elements one by one.

## Usage

Previously, we discussed functions such as `min`, `max`, `sum`, `all`, `any`, etc.
Each of them are happy to receive an iterable (or an iterator).
Typically, you would pass them a list:

```python
lowest_weight = min([person.weight for person in people])

total_cost = sum([item.price for item in shopping_basket])

passed = all([student.grade(course) >= 10 for course in student.courses])
```

While this approach is certainly correct, it can be a bit inefficient:

* first of list is constructed in memory
* this list is passed to a function (`min`, `sum`, `all`)
* the list is thrown away

If `people`, `shopping_basket` or `student.courses` contain many elements, a lot of memory could have been allocated.
Using iterators, however, would avoid this overhead: only one element at a time needs to reside in memory:
Such iterators can be constructed using generator comprehensions:

```python
lowest_weight = min((person.weight for person in people))

total_cost = sum((item.price for item in shopping_basket))

passed = all((student.grade(course) >= 10 for course in student.courses))
```

Python allows you to omit the comprehensions parentheses in such cases:

```python
lowest_weight = min(person.weight for person in people)

total_cost = sum(item.price for item in shopping_basket)

passed = all(student.grade(course) >= 10 for course in student.courses)
```

## Tasks

* Define a function `is_prime(n)` that checks if `n` is a prime number.
* Define a function `primes()` that returns an iterator of all primes.

```python
>>> is_prime(5)
True

>>> is_prime(6)
False

>>> ps = primes()
>>> next(ps)
2

>>> next(ps)
3

>>> next(ps)
5

>>> next(ps)
7
```
