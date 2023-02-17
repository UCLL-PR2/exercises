import pytest
from pytest import approx
from math import pi
from student import *


@pytest.mark.parametrize('width,length,expected_perimeter,expected_area', [
    (1, 1, 4, 1),
    (1, 2, 6, 2),
    (2, 4, 12, 8),
])
def test_rectangle(width, length, expected_perimeter, expected_area):
    rectangle = Rectangle(width=width, length=length)
    assert expected_perimeter == rectangle.perimeter
    assert expected_area == rectangle.area


@pytest.mark.parametrize('side,expected_perimeter,expected_area', [
    (1, 4, 1),
    (2, 8, 4),
    (3, 12, 9),
])
def test_square(side, expected_perimeter, expected_area):
    square = Square(side=side)
    assert expected_perimeter == square.perimeter
    assert expected_area == square.area


@pytest.mark.parametrize('radius,expected_perimeter,expected_area', [
    (1, 2 * pi, pi),
    (2, 4 * pi, 4 * pi),
    (3, 6 * pi, 9 * pi),
])
def test_circle(radius, expected_perimeter, expected_area):
    circle = Circle(radius=radius)
    assert expected_perimeter == approx(circle.perimeter)
    assert expected_area == approx(circle.area)


def test_shape_cannot_be_instantiated():
    with pytest.raises(TypeError):
        Shape()


def test_rectangle_is_shape():
    rectangle = Rectangle(2, 5)
    assert isinstance(rectangle, Shape)


def test_square_is_rectangle():
    square = Square(2)
    assert isinstance(square, Rectangle)


def test_circle_is_shape():
    circle = Circle(2)
    assert isinstance(circle, Shape)
