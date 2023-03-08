---
layout: page
show_in_header: yes
title: Workflow
---

# Table of Contents

* Table of Contents
{:toc}

# Structure

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
```

The "deepest" directories correspond to exercises.
Each exercise resides in its own directory.

# Solving an Exercise

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

# Saving Your Exercises in your Repository

Normally, you should only be modifying `student.py` files.
You _can_ modify other files if you wish, but that might cause problems if we were to update those same files ourselves.
This explanation assumes you will only store your `student.py` files in the repository.

To store your solutions in your repository and upload them to GitHub, follow these steps:

```bash
# Go to the exercise's directory

# Tell Git that you want to keep this new version of student.py
$ git add student.py

# Next, commit your change to the repository. The message is mandatory, but it can be anything you wish
$ git commit -m 'solved exercise on properties'

# At this point, the update is stored in your local repository (the one on your machine)
# We now upload (push) it to GitHub
$ git push
```

## Committing Multiple Exercises at Once

If you have a bunch of `student.py` files that you want to commit, you don't need to deal with them one at a time.
Go to your repository's root directory and enter

```bash
# Add all student.py files in one go
$ find . -name "student.py" | xargs git add
$ git commit -m 'MESSAGE'
$ git push
```

# Getting Updates

When we add or update material, we do this in our own lecturer's repository, the one at `https://github.com/UCLL-PR2/exercises`.
However, these updates do not come automatically to you.

We assume that you followed our installation instructions correctly.

```bash
$ git pull upstream main
```

If this command succeeds, you have the most recent updates.
There are two main ways things can go wrong.

**Error 1: unknown remote**
```bash
$ git pull upstream main
fatal: 'upstream' does not appear to be a git repository
fatal: Could not read from remote repository.
```

If you get the error message above, it means you haven't set up your remotes correctly.
Enter

```bash
$ git remote add upstream https://github.com/UCLL-PR2/exercises
```

then try again.

**Error 2: uncommitted changes**

Git wants to be certain that it doesn't overwrite any of your work: the `pull` command will only work if Git is certain this is indeed the case.
You will need to `add` and `commit` your changes before `pull`ing.
This will ensure that your code cannot get lost.

To get an idea of which files are still uncommitted, you can use

```
$ git status
```
