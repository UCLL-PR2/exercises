# Access Control

## Concepts Used

* Classes
* Access control

## Some Explanation

Objects store their state in attributes, as shown below:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

`Point` objects now have two attributes named `x` and `y` which we can freely access and modify:

```python
pt = Point(3, 5)

# Reading attribute x
print(pt.x) # prints 3

# Modifying attribute y
pt.y *= 2
print(pt.y) # prints 10
```

Let's consider a different class. We want an `Account` class which stores a password.
We feel this password should be hidden somehow, but how can we achieve this?

It's actually rather easy: have the attribute name start with two underscores.
For example,

```python
class SecretHolder:
    def __init__(self, secret):
        self.__secret = secret


secret_holder = SecretHolder('my secret')
secret_holder.secret    # Does not work
secret_holder.__secret  # Does not work either
```

So, by simply changing the attributes name, we can keep it from being seen by the outside world.

# Task

Create a class `Account`.

* It should have a publically accessible attribute `login`.
* It should have a private attribute `password`.
* Both these attributes must be initialized by constructor parameters.
* Provide a method `is_correct_password(self, pw)` that checks if `pw` is equal to the password.

## Important

We have to admit that the `Account` class is actually a _really_ bad example.
We only used it because it is very intuitive to want to hide a password, which gives us an easy to explain reason for as why we would want to hide members.

In reality, "hidden" members are still very easily accessible in Python, so the password is still very much exposed.
Python's method of hiding attributes is not meant as a safety feature, but simply as a way to convey intent.
It protects against Murphy, but not against Machiavelli.

Also, as a general rule, passwords are *never* stored, regardless of the technology used, i.e., this is not a Python-specific rule.
For example, websites such as Google, Amazon, Reddit, etc. never store your password as it would be incredibly unsafe to do so.
If you're wondering how a website can check whether your password is correct without having access to it, feel free to ask your lecturer.
