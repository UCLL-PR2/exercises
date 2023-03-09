# Return Values

Let's do a little bit more with these function-arguments:

```python
def foo():
    return 5


def get_return_value(function):
    return function()


>>> get_return_value(foo)
5
```

Here, `get_return_value` calls the given `function`, which produces a value.
This value is then returned by `get_return_value`.
Again, admittedly, not very useful, but examples should be small.

## Task

Write the following functions:

* `repeat_and_collect(function, n)` calls `function` `n` times and collects the return values in a list.
  In other words, it returns `[function(), function(), function(), ...]`.
* `collect_while(function)` keeps calling `function` as long as it returns a truthy value.
  All returned values are returned in a list, including the last value which was falsey.
