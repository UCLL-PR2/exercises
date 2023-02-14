import unittest
from student import *

class TestRectangleAndSquare(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(4, 5)
        self.square = Square(3)

    def test_rectangle_area(self):
        self.assertEqual(self.rectangle.area(), 20)

    def test_square_area(self):
        self.assertEqual(self.square.area(), 9)

    def test_square_perimeter(self):
        self.assertEqual(self.square.perimeter(), 12)

    def test_square_inherits_from_rectangle(self):
        self.assertIsInstance(self.square, Rectangle)

if __name__ == '__main__':
    unittest.main()
