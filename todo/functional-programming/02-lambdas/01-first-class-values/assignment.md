# First Class Values

Let's consider the value `5`.
What can we _do_ with this value?

We could say, well, we can add it to another integer: `5 + 10`.
We can also multiply it, subtract from it, divide it, compare it, etc.
Plenty of operations are usable on `5`.

Let's generalize this a bit.
Remember that `x + y` is actually translated into `x.__add__(y)`, and `x == y` to `x.__eq__(y)`, etc.
Basically, what we're doing is call a function on `5`.
So the reason we can perform all kinds of operations on `5` is because it can be passed as an argument to a function.

Maybe you're thinking, "well duh, that's not so special at all."
And you would be right.
But bear with us for a moment.

What other "obvious" things can we do with `5`?
Well, we can `return` it from a function!
That's also useful.
And lastly, we can store it in a variable, like with `x = 5`.

A _first class value_ is any "thing" in the language that

* can be stored in a variable
* can be passed as an argument to a function
* can be return as a result from a function

So why do we tell you this?
Why state the obvious?
Maybe it becomes clearer when we take a look at something other than `5`.
There might be values for which it is less obvious that we can do these things.

## First Class Functions

Booleans are clearly first class.
So are strings, lists, tuples, sets, dictionaries, etc.
But what about _functions_?

What can we do with functions?
Most people would say that functions are meant to be "called", meaning we give them a bunch of data (arguments) to work on and we expect a result back.
This "calling" looks like this: `function(arg1, arg2, ...)`.

This `()` syntax can be seen as an operator, just like `+`, `-` and `*` (internally, it is actually also translated to a dunder method, namely `__call__`).
The point is, a function is just another value/object, no more special than `5`, `True` or `"abc"`.

## Assigning Functions to Variables

Consider the code below:

```python
def square(x):
    return x**2
```

This is how you have been defining functions.
Internally, this creates a new variable named `square` and assigns the function to it.
For example, you can interact with `square` as follows:

```python
# Call the function using () syntax
>>> square(5)
25

# Assign the function to another variable
>>> foo = square

# Call the function through foo
>>> foo(3)
9
```

## Passing a Function as Argument

Let's try to pass a function as argument:

```python
def say_hello():
    print("hello")


def call(function):
    function()


>>> call(say_hello)
hello
```

Make sure you understand this code.
There's nothing really  magical about it: `call(f)` simply calls `f`, so it is a rather indirect way of writing `f()`.
Luckily, there's more useful things to do.
But we'll take it one step at a time.

## Task

Write a function `repeat(function, n)` that calls `function` `n` times.

```python
>>> repeat(say_hello, 5)
hello
hello
hello
hello
hello
```
