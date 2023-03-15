# Time Complexity

Disclaimer: time complexity is a actually very tricky topic.
It is very mathematical and can be quite difficult to get right.
Actually, it is a university course on its own.

Fortunately for you, we won't delve too deeply into it.
Our goal is only to have you have a basic understanding of the subject so that you have an idea of what it means when you encounter it.

So, not to worry: this series will remain light on math.

## What is Time Complexity?

The [_time complexity_](https://en.wikipedia.org/wiki/Time_complexity) of an algorithm is a way to describe how fast it goes.
Measuring this "speed" is actually much trickier than it may seem.
Just timing it and saying "this algorithm find a solution in 5 seconds!" means very little.

* The machine on it runs makes a huge difference.
  If you run it on a [80286](https://en.wikipedia.org/wiki/Intel_80286) 8Mhz (your current processor's great great great great grandfather) it will run a bit slower than on your current machine.
* The programming language used can have a large impact on performance.
* The size of the problem matters: did it process 5 bytes or 5 gigabytes of data?
* The actual data used also matters: for example, if you have a billion numbers and need to find out if there's a `5` somewhere in there, the search will end very quickly if the `5` appears at the beginning but long if it does not occur at all.

Time complexity is actually rather vague: it describes how the running time is related to the input size.
Let's try to make this clear with an example.

## `contains_duplicates`

Say we have a list of positive integers and we want to find out if it contains duplicates:

```python
>>> contains_duplicates([4, 2, 5, 3, 7])
False

>>> contains_duplicates([4, 2, 5, 3, 7, 5])
True    # Because 5 occurs twice
```

Let's write an algorithm for this.
Our first attempt is

```python
def contains_duplicates1(ns):
    found_duplicates = False
    for i in range(len(ns)):
        for j in range(len(ns)):
            if i != j and ns[i] == ns[j]:
                found_duplicates = True
    return found_duplicates
```

It is important that you know how this algorithm works, so take your time to understand it:
the main idea is that `contains_duplicates1` compares every element with every other element.

We now want an idea how many "instructions" are executed.
Let's keep this simple and count how many times the `if` statement is executed.

Say `len(ns) == 2`. What are the different values `i` and `j` can take on?

| `i` | `j` |
|-|-|
| `0` | `0` |
| `0` | `1` |
| `1` | `0` |
| `1` | `1` |

This means the `if` statement is executed four times.
What if `len(ns) == 3`?

| `i` | `j` |
|-|-|
| `0` | `0` |
| `0` | `1` |
| `0` | `2` |
| `1` | `0` |
| `1` | `1` |
| `1` | `2` |
| `2` | `0` |
| `2` | `1` |
| `2` | `2` |

Nine possible combinations, which means the `if` statement is also executed nine times.
You probably see a pattern here: given a list `ns`, the algorithm will perform `len(ns)`<sup>2</sup> steps (where step=the `if` statement.)

We say that this algorithm is _quadratic_ because the number of steps is the square of the size of the input:

| `len(ns)` | steps |
|-|-|
| 1 | 1 |
| 2 | 4 |
| 3 | 9 |
| 4 | 16 |
| 5 | 25 |
| 6 | 36 |

In other words: if you _double_ the size of the input list, the algorithm takes _four_ times as much time.

You could object and say we forgot about the `return`: that's an extra step!
Well, yes, that's true, so we should really say

| `len(ns)` | steps |
|-|-|
| 1 | 2 |
| 2 | 5 |
| 3 | 10 |
| 4 | 17 |
| 5 | 26 |
| 6 | 37 |

But in reality, this extra step doesn't matter.
The speed of an algorithm only matters if the inputs are large, in the order of millions or billions.
Once we're there, this extra step really makes no difference.

| `len(ns)` | steps |
|-|-|
| 10,000 | 100,000,000 |
| 20,000 | 400,000,000 |
| 50,000 | 2,500,000,000 |

So even it it's `len(ns)`<sup>2</sup>`+1`, we simpliy it to `len(ns)`<sup>2</sup>.

## First Improvement

We can improve this algorithm quite a bit.
A first improvement could be that we stop searching as soon as we find a duplicate.

```python
def contains_duplicates2(ns):
    for i in range(len(ns)):
        for j in range(len(ns)):
            if i != j and ns[i] == ns[j]:
                return True
    return False
```

This way, if `ns == [1, 1, 4, 2, 10 billion more elements]`, it will only take 2 steps (`i=0, j=0` and `i=0, j=1`).
Now things become a bit more complicated, because we should take into account all possible placements for the duplicates, and calculate average number of steps needed.
We're not going to do that here.
Instead, we just go for worst case: what's the maximum number of steps the algorithm could need?
Well, if there are _no_ duplicates, then it will have to look at all pairs, and we're back to `len(ns)`<sup>2</sup>.

## Second Improvement

Right now `i` and `j` take on all possible combinations of indices, but we can cut that in half.
See, if `i = 2` and `j = 5`, there's no need to later check `i = 5` and `j = 2`.
If `ns[2] != ns[5]`, we can be certain that `ns[5] != ns[2]` too.

We adapt our code so that `i` still goes through all indices, but `j` stays "on the right" of `i`, it only takes on higher indices: `i < j`.

```python
def contains_duplicates3(ns):
    for i in range(len(ns)):
        # j goes from i+1 to end instead of 0 to end
        for j in range(i + 1, len(ns)):
            if ns[i] == ns[j]:
                return True
    return False
```

Using this optimization, we have reduced the number of steps from `len(ns)`<sup>2</sup> to `len(ns)`<sup>2</sup>`/2`.
That's great, and it definitely will make a difference.

However, if you do the math, you will see that an input twice the size will still lead to four times the number of steps.

| `len(ns)` | `len(ns)`<sup>2</sup> | `len(ns)`<sup>2</sup>`/2` |
|:-:|:-:|:-:|
| 2 | 4 | 2 |
| 4 | 16 | 8 |
| 8 | 64 | 32 |
| 16 | 256 | 128 |

Time complexity is only interested in this ratio, namely that input &times; 2 means steps &times; 4.
For a time complexity point of view, the optimization has made no difference.

So this is one example of how time complexity does not necessarily coincide with your expectations.
We've clearly made an optimization, yet it does not count as one.

Does this mean that time complexity is useless?
Of course not.
When the time complexity _does_ go down, it will mean that the optimization is far more effective.
This optimization simply is "too small" to be noticed by time complexity.

## Getting that Time Complexity Down

Let's cheat for a moment: let's assume that `ns` is _sorted_!
Finding duplicates becomes much easier then: if they occur, they will be next to each other.

```python
def contains_duplicates4_cheat(ns):
    for i in range(1, len(ns)):
        if ns[i-1] == ns[i]:
            return True
    return False
```

We ditched `j` and only have `i` go over the list.
If we count the number of steps needed in worst case (no duplicates), we get

| `len(ns)` | steps |
|:-:|:-:|
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |
| 4 | 4 |
| 10000 | 10000 |
| 50000 | 50000 |

This is quite an improvement!
This is called _linear_: if the input doubles, the number of steps also doubles.
The time complexity has now indeed gone down from `len(ns)`<sup>2</sup> to just `len(ns)`.

Let's use a more official notation: typically, the size of the input is denoted `n`.
In other words, instead of writing `len(ns)` each time, we simply write `n`.
The time complexity is then written as O(n<sup>2</sup>) for quadratic or O(n) for linear.

But, we _did_ cheat a bit: we sorted the list.
So technically, our solution should be written

```python
def contains_duplicates4(ns):
    ns = sorted(ns)  # We sort the list
    for i in range(1, len(ns)):
        if ns[i-1] == ns[i]:
            return True
    return False
```

This sorting is bound to take some time.
The total time is now time_for_sorting(n) + n, which might actually be greater than n<sup>2</sup>...

Good news!
Sorting is actually relatively fast and its time complexity is O(n &times; log(n)), which we'll write O(n log n) for short.
To give you an idea, here's a table with values comparing it to O(n) and O(n<sup>2</sup>):

| n | O(n) | O(n log n) | O(n<sup>2</sup>) |
|:-:|:-:|:-:|:-:|
| 1024 | 1024 | 10,240 | 1,048,576 |
| 2048 | 2048 | 22,528 | 4,194,304 |
| 4096 | 4096 | 49,152 | 16,777,216 |
| 8192 | 8192 | 106,496 | 67,108,864 |

As you can see, O(n log n) is actually quite much closer to O(n) than O(n<sup>2</sup>).
Our time complexity this becomes O(n log n + n).
We can actually simplify this to just O(n log n) for the same reason that O(n<sup>2</sup> + 1) is the same as O(n<sup>2</sup>): for large inputs, the +n part will become negligible in comparison with the n log n part.

So, okay, our newest version isn't linear, it's O(n log n) instead, but as the table above shows, it's still a great improvement.
For lists of 8192 items (which is still quite small) it's 1000&times; faster!
For bigger lists, this factor becomes even greater: for one billion elements, it's around 10 million times faster.
We hope you understand now why the previous optimization was actually peanuts, a mere halving of the execution time.

## Linear Time

We can still do better.

```python
def contains_duplicates5(ns):
    previously_seen = set()
    for i in range(0, len(ns)):
        if ns[i] in previously_seen:
            return True
        else:
            previously_seen.add(ns[i])
    return False
```

Here, we go through the list from left to right.
`previously_seen` is a _set_ in which we will store all elements we encounter.
For every element, we will first check if it's already in the set `previously_seen`.
If so, it means we have a duplicate and can `return True`.
Otherwise we add the new number to the set and proceed with the next number.

Our code looks linear: we only have `i` that goes from beginning to end.
However, maybe there's a new kind of cheat, like the sorting in the previous version: we do interact with the set, and that could be slow.

The question is now: how long does it take to check if an element is in a set (`ns[i] in previously_seen`) and how long does it take to add a new value to a set (`previously_seen.add(ns[i]))`).
Let's call those times A and B for now.
The time complexity becomes then O(n &times; (A+B)), because we check and add for every element (worst case scenario).

Sets are actually quite great: they are optimized for exactly these two operations.
Checking for membership and adding an element happens in _constant time_: O(1).
In other words, A and B are equal to 1, making the total time complexity O(2 n), which can be simplified to O(n).

Using a list instead of a set would not work as well and bring us back to O(n<sup>2</sup>).
This is due to the fact that checking if an item is in a list is slow, namely O(n), so in total it would lead to O(n (n + 1)) = O(n<sup>2</sup>).

Lists are slow because in order to find an element, you have to go through the entire list.
If the list has N elements, you need N steps, hence O(n).
A set, however, is smarter and internally organizes its elements differently, making it possible to know if it contains a certain value in a single step: O(1).

## Better Still?

Going under linear time is sadly impossible.
It would mean that we do not have to visit all elements in the input list, but we simply cannot avoid that.
For example, `[1, 2, 4, 5, 6, ..., 1000000000, 1]`: if we ignore the last element, there are no duplicates.
But this would be a wrong answer: the list _does_ contain `1` twice.
In other words, we cannot afford to skip a single element, which means that O(n) is the best we can do.

## Task

You are given a `benchmark` function (see `starter-code.py`).
You can use it as follows:

```python
>>> lst = [1, 2, 3, 4, 5]
>>> benchmark(contains_duplicates1, lst)
2.3399945348501205e-05
```

It calls `contains_duplicates1(lst)` ten times and returns the total execution time.

Copy `benchmark`'s definition to `student.py` as well as all our versions of `contains_duplicates`.
Check the following things:

* Compare execution times of `contains_duplicates1` on a lists `list(range(1000))`, `list(range(2000))` and `list(range(4000))`.
  Check if it fits our predictions.
* Compare execution times of `contains_duplicates2` on the same lists.
  Check again if it fits our predictions.
* Compare execution times of `contains_duplicates3` on the same lists.
  Check again if it fits our predictions.
* Compare execution times of all versions on `list(range(5000))`.
  One of the measurements should surprise you as it seemingly contradicts our explanations above.
* Shuffle the previously used list randomly (using `random.shuffle`) and measure the times again.
  The "surprise" should be gone.
  Can you explain what happened?
