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
@pytest.mark.parametrize('position, color, move', [
    *(
        (
            Position(x, y),
            'white',
            Position(x, y + 1)
        )
        for x in range(0, 8)
        for y in range(0, 7)
    ),
    *(
        (
            Position(x, y),
            'black',
            Position(x, y - 1)
        )
        for x in range(0, 8)
        for y in range(1, 8)
    ),
])
def test_pawn_legal_move(position, color, move):
    pawn = Pawn(position=position, color=color)
    pawn.move(move)
    assert pawn.position == move


@if_class_exists('Pawn')
@pytest.mark.parametrize('position, color, move', [
    *(
        (
            Position(x1, y1),
            'white',
            Position(x2, y2)
        )
        for x1 in range(0, 8)
        for x2 in range(0, 9)
        for y1 in range(0, 7)
        for y2 in range(0, 9)
        if x1 != x2 or y1 + 1 != y2 or y2 > 7
    ),

])
def test_pawn_white_illegal_move(position, color, move):
    pawn = Pawn(position=position, color=color)
    with pytest.raises(ValueError):
        pawn.move(move)
    assert pawn.position == position


@if_class_exists('Pawn')
@pytest.mark.parametrize('position, color, move', [
    *(
        (
            Position(x1, y1),
            'black',
            Position(x2, y2)
        )
        for x1 in range(0, 8)
        for x2 in range(0, 9)
        for y1 in range(0, 7)
        for y2 in range(-1, 8)
        if x1 != x2 or y1 - 1 != y2 or y2 < 0
    ),

])
def test_pawn_black_illegal_move(position, color, move):
    pawn = Pawn(position=position, color=color)
    with pytest.raises(ValueError):
        pawn.move(move)
    assert pawn.position == position


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
@pytest.mark.parametrize('position, color, move', [
    *(
        (
            Position(x, y),
            color,
            Position(x + dx, y + dy)
        )
        for x in range(0, 8)
        for y in range(0, 8)
        for dx in [-1, 0, 1]
        for dy in [-1, 0, 1]
        if dx != 0 or dy != 0
        if 0 <= x + dx < 8 and 0 <= y + dy < 8
        for color in ['black', 'white']
    ),
])
def test_king_legal_move(position, color, move):
    pawn = King(position=position, color=color)
    pawn.move(move)
    assert pawn.position == move


@if_class_exists('King')
@pytest.mark.parametrize('position, color, move', [
    *(
        (
            Position(x1, y1),
            color,
            Position(x2, y2)
        )
        for x1 in range(0, 8)
        for y1 in range(0, 8)
        for x2 in range(0, 8)
        for y2 in range(0, 8)
        if abs(x1 - x2) > 1 or abs(y1 - y2) > 1 or (x1 == x2 and y1 == y2)
        for color in ['black', 'white']
    ),
])
def test_king_illegal_move(position, color, move):
    pawn = King(position=position, color=color)
    with pytest.raises(ValueError):
        pawn.move(move)
    assert pawn.position == position
