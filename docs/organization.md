---
layout: page
show_in_header: true
---
# Organization

The exercises are organized in a directory structure.
If you look at the course material you [previously downloaded](installation/get-exercises.md), you'll find the following structure (this may not be an exact match, we might have changed things a tiny bit):

```text
01-basic-python
    01-arithmetic
        01-five
        02-square
        03-cakes
    02-conditionals
        01-sign
        02-card-value
        03-between
    ...
02-oo
    01-access-control
        01-account
        02-queue
    02-properties
        01-readonly
        02-computed-attribute
        03-setters
        ...
    ...
```

The "deepest" directories correspond to exercises; each exercise resides in its own directory.

The first exercise is `01-basic-python/01-arithmetic/01-five`.
Open it in Visual Studio Code.
You'll find a number of files there:

* `assignment.md` explains what the exercise is about and what you should do.
* `student.py` is an empty file where you should write your code.
* `tests.py` contains tests that check the code you've added in `student.py`.
* `solution.py` contains a possible solution.
  You really should only be looking at this after you managed to solve the exercise.

So, to solve an exercise, first read `assignment.md`, write code in `student.py` and run the tests.
You can run the tests as follows:

```bash
# You must reside in the exercise's directory
$ pytest
```

An exercise is solved correctly if all tests have passed and zero tests have been skipped.
A skipped test typically means that you have not implemented everything the `assignment.md` asked for.
