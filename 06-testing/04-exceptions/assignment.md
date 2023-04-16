# Exceptions

When calling a function with invalid arguments, the function will raise an exception.
This aspect of its behavior should also be tested.

## Book

In `book.py`, write a class `Book` with two readonly properties: `title` and `isbn`.
The following rules must be enforced:

* `title` must not be empty.
* `isbn` must be a valid ISBN number (see below)

If either of the arguments is invalid, a `RuntimeError` must be thrown.


Usage example:

```python
# Valid Book creation
>>> book = Book('Watchmen', '978-1779501127')

# Invalid title
>>> book = Book('', '978-1779501127')
RuntimeError

# Invalid ISBN
>>> book = Book('Watchmen', '978-1779501128')
RuntimeError
```

### ISBN Validity

The ISBN of a book consists of 13 digits, which can be separated by spaces or dashes (`-`).
Additionally, in order to detect mistakes, the last digit acts as a checksum.

The checksum algorithm goes as follows:

* Let's say we store the digits in an array `digits`.
  This array has length 13.
* Multiply the odd-indexed digits by 3.
* Take the sum of `digits`.
* This sum must be divisible by 10.

For example, consider the valid ISBN `978-1779501127`.
The `digits` array is `[9, 7, 8, 1, 7, 7, 9, 5, 0, 1, 1, 2, 7]`.
Multiplying the odd-indexed digits yields `[9, 21, 8, 3, 7, 21, 9, 15, 0, 3, 1, 6, 7]`.
The sum is `9 + 21 + 8 + 3 + 7 + 21 + 9 + 15 + 0 + 3 + 1 + 6 + 7 = 110`
This number is divisible by 10, meaning the ISBN is valid.

## Testing

In `tests.py`, write three parametrized tests:

* `test_valid_creation` that create books with valid `title` and `isbn`.
* `test_creation_with_invalid_title` that create books with an invalid `title`.
* `test_creation_with_invalid_isbn` that create books with an invalid `isbn`.

But how does one assert that an exception is thrown?
Pytest offers the following construct:

```python
import pytest


def test_raises_exception():
    with pytest.raises(ExceptionClass):
        # code that should throw an ExceptionClass
```

Keep the code inside the `with` block to a minimum.
The more code there is, the more potential sources of exceptions there are.
You want to make sure it's the right function that raises the exception.

In order to write the tests, you'll need both valid and invalid ISBNs.

* You can easily find valid ISBNs online.
* Modifying a single digit of a valid ISBN gives an invalid ISBN.
* Having more or less than 13 digits also invalidates an ISBN.

Make sure that you check all possible ways that an ISBN can be invalid.
For example, if you only check for exceptions using ISBNs with 14 digits, then you don't know if an exception will be thrown if an ISBN with a faulty checksum is used.

You can check your work using our own tests:

```bash
$ pytest verify.py
```
