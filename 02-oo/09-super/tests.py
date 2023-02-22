import pytest
from pytest import approx
from math import pi
from solution import *


def if_class_exists(class_name):
    return pytest.mark.skipif(class_name not in globals(), reason=f'{class_name} is not defined')


@if_class_exists('Rectangle')
@pytest.mark.parametrize('width,length,expected_perimeter', [
    (1, 1, 4),
    (1, 2, 6),
    (2, 4, 12),
])
def test_rectangle_perimeter(width, length, expected_perimeter):
    rectangle = Rectangle(width=width, length=length)
    assert expected_perimeter == rectangle.perimeter


@if_class_exists('Rectangle')
@pytest.mark.parametrize('width,length,expected_area', [
    (1, 1, 1),
    (1, 2, 2),
    (2, 4, 8),
])
def test_rectangle_area(width, length, expected_area):
    rectangle = Rectangle(width=width, length=length)
    assert expected_area == rectangle.area


@if_class_exists('Rectangle')
@pytest.mark.parametrize('property_name', [
    'width',
    'length',
    'perimeter',
    'area',
])
def test_rectangle_properties_are_readonly(property_name):
    rectangle = Rectangle(width=1, length=2)
    with pytest.raises(AttributeError):
        setattr(rectangle, property_name, 2)


@if_class_exists('Rectangle')
def test_rectangle_is_shape():
    assert Shape in Rectangle.__mro__


@if_class_exists('Square')
@pytest.mark.parametrize('side,expected_perimeter', [
    (1, 4),
    (2, 8),
    (3, 12),
])
def test_square_perimeter(side, expected_perimeter):
    square = Square(side=side)
    assert expected_perimeter == square.perimeter


@if_class_exists('Square')
@pytest.mark.parametrize('side,expected_area', [
    (1, 1),
    (2, 4),
    (3, 9),
])
def test_square_area(side, expected_area):
    square = Square(side=side)
    assert expected_area == square.area


@if_class_exists('Square')
@pytest.mark.parametrize('property_name', [
    'width',
    'length',
    'perimeter',
    'area',
])
def test_square_properties_are_readonly(property_name):
    rectangle = Square(side=1)
    with pytest.raises(AttributeError):
        setattr(rectangle, property_name, 2)


@if_class_exists('Square')
def test_square_is_rectangle():
    assert Rectangle in Square.__mro__


# @pytest.mark.parametrize('side,expected_perimeter,expected_area', [
#     (1, 4, 1),
#     (2, 8, 4),
#     (3, 12, 9),
# ])
# def test_square(side, expected_perimeter, expected_area):
#     square = Square(side=side)
#     assert expected_perimeter == square.perimeter
#     assert expected_area == square.area


# @pytest.mark.parametrize('radius,expected_perimeter,expected_area', [
#     (1, 2 * pi, pi),
#     (2, 4 * pi, 4 * pi),
#     (3, 6 * pi, 9 * pi),
# ])
# def test_circle(radius, expected_perimeter, expected_area):
#     circle = Circle(radius=radius)
#     assert expected_perimeter == approx(circle.perimeter)
#     assert expected_area == approx(circle.area)


# def test_shape_cannot_be_instantiated():
#     with pytest.raises(TypeError):
#         Shape()


# def test_rectangle_is_shape():
#     rectangle = Rectangle(2, 5)
#     assert isinstance(rectangle, Shape)


# def test_square_is_rectangle():
#     square = Square(2)
#     assert isinstance(square, Rectangle)


# def test_circle_is_shape():
#     circle = Circle(2)
#     assert isinstance(circle, Shape)
