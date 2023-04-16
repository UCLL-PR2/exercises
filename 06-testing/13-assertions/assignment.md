# Assertions

You've been using `assert` to perform checks in your tests.
But what exactly does `assert` do?

```python
assert condition, message
```

can be translated

```python
if not condition:
    raise AssertionError(message)
```

No big surprises here.
However, there's slightly more to it than that.

## Debug vs Release Builds

The only language your processor understands is machine code.
However, writing machine code directly is *very* hard.
For this reason, we developed programming languages such as C, C++, Python, Ruby, C#, Java, JavaScript, etc.
Code written in these languages need to be translated into machine code.
Programs performing these translations are called [interpreters](https://en.wikipedia.org/wiki/Interpreter_(computing)) or [compilers](https://en.wikipedia.org/wiki/Compiler).
They do differ in the approach they take, but we won't go into detail here.
From now on, we'll use the word "compile" and "compiler" to mean "translate" and "translator program".

A common misconception is the belief that the compilation from programming language to machine code happens "literally", i.e., word-for-word translations, without changes.
In reality, compilers have a lot of freedom:

* They can eliminate [dead code](https://en.wikipedia.org/wiki/Dead_code), i.e., code that is never used.
* They can change the order of instructions as this can potentially make the program run faster.
  This can be as basic as swapping two statements but can be as advanced as modifying your loops.
  Of course, this only happens if the compiler can determine it does not change the observable behavior of the program.
* If your code evaluates the same expression twice, a compiler can choose to reuse to result of the first evaluation.
* Algorithms can be rewritten into a more efficient, behaviorally equivalent form.

The compiled form might barely bear any resemblance to your original code.
An advantage of this is that your program will run faster and consume less memory than if executed "literally".
A downside, however, is that it can make debugging much harder.
To find a bug, you might want to execute your code step by step using a debugger, but if all instructions have been reordered or even rewritten, this might not be possible anymore.

For this reason, we make the distinction between a debug build and a release build:

* In the debug build, no optimizations are made.
  The code is compiled in a very straightforward manner, and possibly extra metadata is added to assist you in debugging.
* In a release build, all optimizations are turned on and none of the debugging aids are present.
  This is the build the end user will receive.

For example, in a language like C++ the gap between debug and release build is huge.
In the debug build, plenty of checks are made so as to catch bugs quickly.
In the release build, no checks are made, as it is assumed the code is bug free.
As a result, the release build often runs 10 to 100 times faster.

In Python, the difference between debug and release build is much smaller, almost nonexistent even.
The most significant difference is how [`assert`s are executed](https://docs.python.org/3/reference/simple_stmts.html#assert): in release mode the `assert`s are ignored.

Say the following code is stored in `demo.py`:

```python
assert False, 'Failure!'
```

Running it gives

```bash
$ py demo.py
AssertionError: Assertion failure!
```

However, running it in release mode (called optimized mode in Python) gives

```bash
$ py -O demo.py
# Nothing happens
```

It is therefore crucial that you do not rely on `assert` for anything that actually impacts behavior.
`assert` is merely to be used as a debugging aid.
For the purposes of testing, using `assert` is of course safe: there's no reason to run tests is release build.

## When to Use `assert`

`assert` can be used in regular code, i.e., not testing code, to perform self-checks.
For example, the code for `max` could look as follows:

```python
def max(ns):
    result = ns[0]
    for n in ns:
        if n > result:
            result = n

    # Check that result is an element of the given list
    assert result in ns
    # Check that all values in the given list are not greater than result
    assert all(n <= result for n in ns)

    return result
```

Here's another example: the function `median` checks its result before returning it.
There could still be a bug in the algorithm despite the `assert` condition being true, but that's okay: partial checks are valuable too.

```python
def median(ns):
    sorted_ns = sorted(ns)
    if len(ns) % 2 == 0:
        right_of_center = len(ns) // 2
        left_of_center = right_of_center - 1
        result = (sorted_ns[left_of_center] + sorted_ns[right_of_center]) / 2
    else:
        center = len(ns) // 2
        result = sorted_ns[center]

    # Check that there are as many elements "below" result as there are elements "above" result
    assert sum(1 for n in ns if n <= result) == sum(1 for n in ns if n >= result)
    return result
```

## `assert` vs Tests

`assert`s in regular code perform plenty of checks as the program is running.
While they perform a job very similar as that of tests, they do *not* replace tests.
They're just an extra way of checking your code.

## Task

`starter.py` contains (correct) code for merge sort.
Copy it to `student.py`.
Add `assert`s where you can.
If an `assert` condition becomes complex, don't hesitate to define a separate function for it, which the `assert` can then call.
Compare it with our solution.
Make sure to understand what each `assert` checks.
