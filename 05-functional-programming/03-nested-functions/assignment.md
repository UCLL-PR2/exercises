# Nested Functions

Let's revisit an old example:

```python
def is_made_by_spielberg(movie):
    return movie.director == 'Steven Spielberg'


def count_films_by_spielberg(movies):
    return count(movies, is_made_by_spielberg)
```

We had to define a separate little function `is_made_by_spielberg` to be passed to `count`.
This feels rather clumsy.

What if we want to write a function `count_films_by_director(movies, director)` and rely on `count` in the process?
Let's try...

```python
def is_made_by_director(movie):
    return movie.director == director


def count_films_by_director(movies, director):
    return count(movies, is_made_by_director)
```

This won't work: we mean `is_made_by_director` to refer to `count_films_by_director`'s second parameter, but Python will not understand it that way.
Parameters are by definition local and only accessible within the corresponding function.
So, how can we give `is_made_by_director` access to `director`?

Well, we just said that parameters are only visible inside the corresponding function.
That's the solution!
We can move `is_made_by_director` inside `count_films_by_director`!

```python
def count_films_by_director(movies, director):
    def is_made_by_director(movie):
        return movie.director == director

    return count(movies, is_made_by_director)
```

This is called a _nested_ or _inner_ function.
This has two consequences:

* `is_made_by_director` can now access variables inside `count_films_by_director` such as `movies` and `director`.
* `is_made_by_director` is only accessible from within `count_films_by_director`: it is essentially a local variable.

## Tasks

Write the following functions:

* `count_older_than(people, min_age)` counts the number of people who are older than `min_age`.
* `indices_of_cards_with_suit(cards, suit)` returns the indices of all the `Card`s whose suit equals `suit`.

Rely on previously defined higher order functions.
