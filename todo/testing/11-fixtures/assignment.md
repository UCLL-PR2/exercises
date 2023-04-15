# Fixtures

We used `setup_function` to factor out common code.
However, it has some serious shortcomings.

> But why did we bother explaining `setup_function` instead of immediately offering the better solution?
> Well, other testing frameworks only provide the `setup_function` approach, and you might always encounter tests that still rely on `setup_function` in older code.



## Shortcomings of `setup_function`

### Failure Bottleneck

`setup_function` gets run before every test.
If it fails, the test cannot run.
It is therefore crucial to make ensure it doesn't fail.
To achieve this, `setup_function` should not interact in any way with the class(es) that are being tested.
In other words, only well-tested code should be used inside the `setup_function`.

### Lack of Readability

Consider the following code:

```python
def setup_function():
    task = Task('description', date(2000, 1, 1))

# many lines of code in between

def test_creation():
    assert task.description == 'description'
    assert task.date == date(2000, 1, 1)
    assert not task.finished
```

By separating the actual Arrange stage from the Assert stage, the latter becomes hard to understand.
It's riddled with magic constants and it makes no sense that "a" task's members has such specific values.

An improvement would be

```python
def setup_function():
    unfinished_task = Task('description', date(2000, 1, 1))

# many lines of code in between

def test_creation():
    assert not unfinished_task.finished
```

Here, the identifier actually conveys information about the `Task` object and it makes sense that an unfinished task's `finished` member is `False`.
However, we run into new problems: