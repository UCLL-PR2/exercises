import pytest
from position import Position
from solution import *


def if_class_exists(class_name):
    return pytest.mark.skipif(class_name not in globals(), reason=f'{class_name} is not defined')


@if_class_exists('Pawn')
@pytest.mark.parametrize('x', range(0, 8))
@pytest.mark.parametrize('y', range(0, 8))
@pytest.mark.parametrize('color', ['black', 'white'])
def test_pawn_valid_creation(x, y, color):
    pawn = Pawn(
        position=Position(x, y),
        color=color)
    assert pawn.position == Position(x, y)
    assert pawn.color == color


@if_class_exists('Pawn')
@pytest.mark.parametrize('position', [
    Position(-1, 0),
    Position(8, 0),
    Position(0, -1),
    Position(0, 8),
])
def test_pawn_creation_invalid_position(position):
    with pytest.raises(ValueError):
        Pawn(position=position, color='white')


@if_class_exists('Pawn')
def test_pawn_creation_invalid_color():
    with pytest.raises(ValueError):
        Pawn(position=Position(0, 0), color='red')


@if_class_exists('Pawn')
@pytest.mark.parametrize('position, color, expected', [
    *(
        (
            Position(x, y),
            'white',
            {Position(x, y + 1)}
        )
        for x in range(0, 8)
        for y in range(0, 7)
    ),
    *(
        (
            Position(x, 7),
            'white',
            set()
        )
        for x in range(0, 8)
    ),
    *(
        (
            Position(x, y),
            'black',
            {Position(x, y - 1)}
        )
        for x in range(0, 8)
        for y in range(1, 8)
    ),
    *(
        (
            Position(x, 0),
            'black',
            set()
        )
        for x in range(0, 8)
    ),
])
def test_pawn_legal_moves(position, color, expected):
    pawn = Pawn(position=position, color=color)
    actual = pawn.find_legal_moves()
    assert actual == expected


@if_class_exists('King')
@pytest.mark.parametrize('x', range(0, 8))
@pytest.mark.parametrize('y', range(0, 8))
@pytest.mark.parametrize('color', ['black', 'white'])
def test_king_valid_creation(x, y, color):
    pawn = King(
        position=Position(x, y),
        color=color)
    assert pawn.position == Position(x, y)
    assert pawn.color == color


@if_class_exists('King')
@pytest.mark.parametrize('position', [
    Position(-1, 0),
    Position(8, 0),
    Position(0, -1),
    Position(0, 8),
])
def test_king_creation_invalid_position(position):
    with pytest.raises(ValueError):
        King(position=position, color='white')


@if_class_exists('King')
def test_king_creation_invalid_color():
    with pytest.raises(ValueError):
        King(position=Position(0, 0), color='red')


@if_class_exists('King')
@pytest.mark.parametrize('position, expected', [
    (
        Position(0, 0),
        {
            Position(1, 0),
            Position(1, 1),
            Position(0, 1),
        }
    ),
    (
        Position(7, 0),
        {
            Position(6, 0),
            Position(6, 1),
            Position(7, 1),
        }
    ),
    (
        Position(3, 0),
        {
            Position(2, 0),
            Position(2, 1),
            Position(3, 1),
            Position(4, 1),
            Position(4, 0),
        }
    ),
    (
        Position(5, 5),
        {
            Position(4, 4),
            Position(4, 5),
            Position(4, 6),
            Position(5, 4),
            Position(5, 6),
            Position(6, 4),
            Position(6, 5),
            Position(6, 6),
        }
    ),
])
@pytest.mark.parametrize('color', ['black', 'white'])
def test_king_legal_moves(position, color, expected):
    pawn = King(position=position, color=color)
    actual = pawn.find_legal_moves()
    assert actual == expected