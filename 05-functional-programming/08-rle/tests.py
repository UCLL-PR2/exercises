import pytest
import student


def if_defined(function_name):
    return pytest.mark.skipif(function_name not in dir(student), reason=f'{function_name} has not been defined')


@if_defined('rle_encode')
@pytest.mark.parametrize('input, expected', [
    (
        '',
        []
    ),
    (
        'a',
        [('a', 1)]
    ),
    (
        'aa',
        [('a', 2)]
    ),
    (
        'aaa',
        [('a', 3)]
    ),
    (
        'aaab',
        [('a', 3), ('b', 1)]
    ),
    (
        'aaabcccc',
        [('a', 3), ('b', 1), ('c', 4)]
    ),
    (
        'xyz',
        [('x', 1), ('y', 1), ('z', 1)]
    ),
])
def test_rle_encode(input, expected):
    assert expected == list(student.rle_encode(input))


@if_defined('rle_decode')
@pytest.mark.parametrize('input, expected', [
    (
        [],
        '',
    ),
    (
        [('a', 1)],
        'a',
    ),
    (
        [('a', 2)],
        'aa',
    ),
    (
        [('a', 3)],
        'aaa',
    ),
    (
        [('a', 3), ('b', 1)],
        'aaab',
    ),
    (
        [('a', 3), ('b', 1), ('c', 4)],
        'aaabcccc',
    ),
    (
        [('x', 1), ('y', 1), ('z', 1)],
        'xyz',
    ),
])
def test_rle_decode(input, expected):
    assert [*expected] == list(student.rle_decode(input))


@if_defined('rle_encode')
@if_defined('rle_decode')
@pytest.mark.parametrize('data', [
    "",
    "a",
    "aaaaa",
    "aaaaaaaaa",
    "abababab",
    "aaaabbbaaaacccccccc",
    "xxxxyyyyyyyyyyyyyzzzzzzzzzzzzzzzzzzzz",
    "0123456789",
])
def test_encoding_and_decoding(data):
    encoded = student.rle_encode(data)
    decoded = student.rle_decode(encoded)
    assert data == "".join(decoded)


@if_defined('rle_encode')
@if_defined('rle_decode')
@pytest.mark.parametrize('data', [
    "",
    "a",
    "aaaaa",
    "aaaaaaaaa",
    "abababab",
    "aaaabbbaaaacccccccc",
    "xxxxyyyyyyyyyyyyyzzzzzzzzzzzzzzzzzzzz",
    "0123456789",
])
def test_rle_works_on_iterators(data):
    encoded = student.rle_encode(iter(data))
    decoded = student.rle_decode(encoded)
    assert data == "".join(decoded)
