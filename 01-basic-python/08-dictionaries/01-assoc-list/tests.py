import pytest
from student import *


def test_empty_assoclist_has_length_0():
    al = AssocList()
    assert len(al) == 0


def test_adding_new_keys_increments_length():
    al = AssocList()
    assert len(al) == 0
    al['a'] = 1
    assert len(al) == 1
    al['b'] = 1
    assert len(al) == 2


def test_adding_same_key_does_not_increment_length():
    al = AssocList()
    assert len(al) == 0
    al['a'] = 1
    assert len(al) == 1
    al['a'] = 2
    assert len(al) == 1


def test_membership():
    al = AssocList()
    al['a'] = 'alfa'
    al['b'] = 'beta'
    al['g'] = 'gamma'
    al['d'] = 'delta'

    assert 'a' in al
    assert 'b' in al
    assert 'g' in al
    assert 'd' in al
    assert 'e' not in al


def test_looking_up():
    al = AssocList()
    al['a'] = 'alfa'
    al['b'] = 'beta'
    al['g'] = 'gamma'
    al['d'] = 'delta'

    assert al['a'] == 'alfa'
    assert al['b'] == 'beta'
    assert al['g'] == 'gamma'
    assert al['d'] == 'delta'


def test_looking_up_overwritten_value():
    al = AssocList()
    al[1] = 'one'
    assert al[1] == 'one'

    al[1] = 'un'
    assert al[1] == 'un'


def test_keys():
    al = AssocList()
    al['a'] = 1
    al['b'] = 2

    keys = al.keys
    assert len(keys) == 2
    assert set(al.keys) == {'a', 'b'}

    al['c'] = 3
    keys = al.keys
    assert len(keys) == 3
    assert set(al.keys) == {'a', 'b', 'c'}


def test_values():
    al = AssocList()
    al['a'] = 1
    al['b'] = 2

    values = al.values
    assert len(values) == 2
    assert set(al.values) == {1, 2}

    al['c'] = 3
    values = al.values
    assert len(values) == 3
    assert set(al.values) == {1, 2, 3}
