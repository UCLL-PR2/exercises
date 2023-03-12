# Lambdas

When calling a higher order function like `count`, we need to pass it some function.
Previously, we discussed how it was possible to define this function locally:

```python
def count_films_by_director(movies, director):
    def is_made_by_director(movie):
        return movie.director == director

    return count(movies, is_made_by_director)
```

Having to define local functions like this can become tiring quickly.
Luckily, Python offers a shorter syntax.
Let's do something weird first and let's define `is_made_by_director` using an alternative syntax:

```python
def count_films_by_director(movies, director):
    is_made_by_director = lambda movie: movie.director == director
    return count(movies, is_made_by_director)
```

Let's dissect this weird new thing.

* The name `lambda` comes from [the lambda calculus](https://en.wikipedia.org/wiki/Lambda_calculus), which is a tiny programming language developed around a century ago.
  You can simply pretend lambda means "function".
* `movie` is the parameter of this function.
* What follows the `:` is the body of the function.
  No `return` is necessary, it happens implicitly.

Now, we also know that

```python
x = 5
print(x)

# is the same as

print(5)
```

Let's apply this substitution trick on our function:

```python
def count_films_by_director(movies, director):
    return count(movies, lambda movie: movie.director == director)
```

So, a _lambda_ is nothing more than an anonymous function.
It is used in cases where we need to quickly define a function with the whole `def`
Instead, we define it inline where it's needed.
In essence, it's a throw-away function.
We don't even bother naming it.

Note that lambdas can only be used for very simple functions: the lambda's body is limited to a single expression.
This is a Python-specific limitation: for nontrivial logic, the language wants you to define a named function using `def`.

## Task

Write the following functions, relying on lambdas and on the helper classes/functions provided in `util.py`:

* `group_by_suit(cards)` groups `cards` by their suit.
* `group_by_value(cards)` groups `cards` by their value.
* `partition_by_color(cards)` splits `cards` into two lists: the first list contains only black cards, the second list only red cards.
  The color of a card is determined by its suit: spades and clubs are black, hearts and diamonds are red.
