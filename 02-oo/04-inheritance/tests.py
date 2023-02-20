import pytest
from position import Position
from solution import *


@pytest.mark.skipif('Pawn' not in globals(), reason="Pawn is not defined")
@pytest.mark.parametrize('x', range(0, 8))
@pytest.mark.parametrize('y', range(0, 8))
@pytest.mark.parametrize('color', ['black', 'white'])
def test_pawn_valid_creation(x, y, color):
    pawn = Pawn(
        position=Position(x, y),
        color=color)
    assert pawn.position == Position(x, y)
    assert pawn.color == color


@pytest.mark.skipif('Pawn' not in globals(), reason="Pawn is not defined")
@pytest.mark.parametrize('position', [
    Position(-1, 0),
    Position(8, 0),
    Position(0, -1),
    Position(0, 8),
])
def test_pawn_creation_invalid_position(position):
    with pytest.raises(ValueError):
        Pawn(position=position, color='white')


@pytest.mark.skipif('Pawn' not in globals(), reason="Pawn is not defined")
def test_pawn_creation_invalid_color():
    with pytest.raises(ValueError):
        Pawn(position=Position(0, 0), color='red')


@pytest.mark.skipif('King' not in globals(), reason="King is not defined")
@pytest.mark.parametrize('x', range(0, 8))
@pytest.mark.parametrize('y', range(0, 8))
@pytest.mark.parametrize('color', ['black', 'white'])
def test_king_valid_creation(x, y, color):
    pawn = King(
        position=Position(x, y),
        color=color)
    assert pawn.position == Position(x, y)
    assert pawn.color == color


@pytest.mark.skipif('King' not in globals(), reason="King is not defined")
@pytest.mark.parametrize('position', [
    Position(-1, 0),
    Position(8, 0),
    Position(0, -1),
    Position(0, 8),
])
def test_king_creation_invalid_position(position):
    with pytest.raises(ValueError):
        King(position=position, color='white')


@pytest.mark.skipif('King' not in globals(), reason="King is not defined")
def test_king_creation_invalid_color():
    with pytest.raises(ValueError):
        King(position=Position(0, 0), color='red')
