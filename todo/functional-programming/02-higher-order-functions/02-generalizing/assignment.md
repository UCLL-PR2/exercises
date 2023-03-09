# Generalizing

In the last exercise, we showed how we could construct a very flexible `count` function.
We'll take on a different function in this exercise.

```python
def children_and_adults(people):
    children = []
    adults = []

    for person in people:
        if person.age < 18:
            children.append(person)
        else:
            adults.append(person)

    return (children, adults)
```

This function partitions a given list `people` into two parts: the children (whose `age` is less than 18) and adults (all the rest).
In order to generalize this function, we need to identify which part needs to become a parameter.

An unambitious effort would be

```python
def children_and_adults(people, cutoff_age):
    children = []
    adults = []

    for person in people:
        if person.age < cutoff_age:
            children.append(person)
        else:
            adults.append(person)

    return (children, adults)
```

We turned the `18` into a parameter, allowing us to pick the age (e.g. `16`, `21`, ...) that serves as cutoff point.
We can do better than that though.
Let's replace the entire `if` condition:

```python
def children_and_adults(people, condition):
    children = []
    adults = []

    for person in people:
        if condition(person):
            children.append(person)
        else:
            adults.append(person)

    return (children, adults)
```

We should update the names of the function and variables as there is nothing in this code that ties it specifically to `Person`s.

```python
def partition(xs, condition):
    true_list = []
    false_list = []

    for x in xs:
        if condition(x):
            true_list.append(x)
        else:
            false_list.append(x)

    return (true_list, false_list)
```

## Task

Generalize the following function:

```python
def find_first_book_by_author(books, author):
    for book in books:
        if book.author == author:
            return book
    return None
```
