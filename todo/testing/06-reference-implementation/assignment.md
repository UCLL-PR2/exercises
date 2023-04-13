# Reference Implementation

In a past exercise, we asked you to write a function `merge_sorted(ks, ns)`.
The test looked a bit like this:

```python
@pytest.mark.parametrize(...)
def test_merge_sorted(ks, ns):
    assert merge_sorted(ks, ns) == sorted(ks + ns)
```

The merging functionality was essentially implemented twice:

* `merge_sorted` itself used a more efficient algorithm.
* `sorted(ks + ns)` is a simple but inefficient way to achieve the same.

This idea of having to implementations can come in handy when implementing complex algorithms.
Typically the same problem can be solved in many ways, either using simple but slow algorithms, or using more complex but fast algorithms.
In these circumstances, it can be useful to implement both a simple slow and and a complex fast algorithm and having the tests compare their results:

```python
@pytest.mark.parametrize(...)
def test_some_functionality(inputs):
    expected = simple_but_slow(inputs)
    actual = complex_but_fast(inputs)
    assert expected == actual
```

## Tasks

A `Student` is defined as

```python
class Student:
    def __init__(self, id):
        self.id = id
```

You are given a list of `Student` objects.
It is guaranteed that the `Student`s appear in order of increasing `id` and that all `Student`s have distinct `id`s.
Your job will be to write code that that returns the `Student` whose `id` equals a given `target_id`.
If no such `Student` exists, `None` should be returned.

You want the search to be as efficient as possible.
Below we explain two algorithms: a slow one (but trivial to implement) and a fast one (but trickier to implement.)
To solve this exercise, you'll need to complete these steps:

* Implement the slow algorithm (linear search).
* Implement the fast algorithm (binary search).
* Write tests that thoroughly check that both algorithms produce the same results.

### Linear Search

A linear search does not make use of the fact that the list is sorted by `id`.
It simply starts with the first `Student` and checks its `id`.
If it equals `target_id`, it has found the right `Student` object and returns it.
If not, the algorithm moves on to the next in line.
If the end of the list is reached without finding the student with `id == target_id`, then `None` is returned.

Write a function `linear_search(students, target_id)` that implements this algorithm.
Put this in the file named `search.py`.

### Binary Search

Say we play a game where we pick a number between 0 and 100 and you need to guess it in as few tries as possible.
After each guess, we tell you if our secret number is lower or higher than your guess.

In order to play optimally, your first guess should be 50.
If we say our number is higher, your next guess should be 75, etc.
In other words, you should always guess the halfway number.

Let's try to write this down more formally.
At the beginning of the game, you know that the number will lie between 0 and 100, i.e., in the interval `[0, 100]`.
Computing the middle gives 50, which is your next guess.
Our feedback is "Higher!".
This lets you shrink the interval to `[51, 100]`.
You again compute the middle, which gives 75 (we assume you round down).
If we answer "Lower!", you know that the new interval becomes `[51, 74]`.

Use this same principle to find the correct `Student` object:

* You'll need to keep track of an interval of indices.
  Initially, all indices from `0` to `len(students) - 1` are potential candidates.
  Simply use two variables (e.g., `left` and `right`) to keep track of the bounds of this interval.
* Compute the index in the middle of this interval.
* Look up the `Student` at this index and compare its `id` with `target_id`.
* If `id == target_id` your search is finished, otherwise you'll need to update either `left` or `right` to reflect the fact that the interval has been halved in two.

Implement this as `binary_search(students, target_id)`.
Also put this in the file named `search.py`.

## Testing

Now write a parametrized test in `tests.py`.
It should have two parameters: `students` and `target_id`.

Make sure to include as all special cases you can think of:

* No `Student` with `id == target_id` occurs in the list.
* The `Student` to be found is the first in the list.
* The `Student` to be found is the last in the list.
* The `Student` to be found is in the list, but neither the first or last.
* The `Student`s' `id`s can be consecutive or have gaps in them.
* The `Student` list is empty.
* `target_id` should simply range from a low id (lower than the minimum student id) to a high id (higher than the maximum student id).
