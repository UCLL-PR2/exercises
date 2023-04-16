import pytest
from book import Book


VALID_ISBNS = [
    '9781779501127',
    '9780735611313',
    '9781593275990',
]

VALID_TITLES = [
    'a',
    'b',
    'xyz',
]


def groups(xs, n):
    if n == 1:
        yield [xs]
    else:
        for i in range(1, len(xs)):
            for group in groups(xs[i:], n-1):
                yield [xs[:i], *group]


def valid_isbn_variants(isbn):
    for n in range(1, 4):
        yield from (
            separator.join(gs)
            for gs in groups(isbn, n)
            for separator in '- '
        )


def swaps(xs):
    for i in range(len(xs) - 1):
        x = int(xs[i])
        y = int(xs[i+1])
        if (x + 3 * y - 3 * x - y) % 10 != 0:
            yield "".join([
                *xs[:i],
                xs[i+1],
                xs[i],
                xs[i+2:]
            ])


def digit_modifications(isbn):
    for i in range(len(isbn)):
        yield "".join([
            *isbn[:i],
            str((int(isbn[i]) + 1) % 10),
            isbn[i+1:],
        ])


def invalid_isbn_variants(isbn):
    yield from swaps(isbn)
    yield from digit_modifications(isbn)
    yield f"{isbn}5"
    yield isbn[1:]


@pytest.mark.parametrize('title', VALID_TITLES)
@pytest.mark.parametrize('isbn', (
    isbn
    for base_isbn in VALID_ISBNS
    for isbn in valid_isbn_variants(base_isbn)
))
def test_valid_creation(title, isbn):
    book = Book(title, isbn)

    assert book.title == title
    assert book.isbn == isbn


@pytest.mark.parametrize('isbn', VALID_ISBNS)
def test_creation_with_invalid_title(isbn):
    with pytest.raises(RuntimeError):
        Book('', isbn)


@pytest.mark.parametrize('isbn', (
    isbn
    for base_isbn in VALID_ISBNS
    for isbn in invalid_isbn_variants(base_isbn)
))
def test_creation_with_invalid_isbn(isbn):
    title = 'x'
    with pytest.raises(RuntimeError):
        Book(title, isbn)


# [8,21,9,3,7,21,9,15,0,3,1,6,7]