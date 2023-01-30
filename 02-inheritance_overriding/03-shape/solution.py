class Shape:
    def __init__(self, name):
        self.name = name
    
    def describe(self):
        return f"{self.name} is a 2D shape"

class Triangle(Shape):
    def __init__(self, name, sides):
        super.__init__(self, name)
        self.sides = sides
    
    def describe(self, type="scalene"):
        return f"{self.name} is a {type} triangle with {self.sides} sides"

class Rectangle(Shape):
    def __init__(self, name, sides):
        super.__init__(self, name)
        self.sides = sides
    
    def describe(self, type="not a square"):
        return f"{self.name} is a {type} rectangle with {self.sides} sides"

triangle = Triangle("Isosceles", 3)
triangle.describe(type="isosceles") # Isosceles is a isosceles triangle with 3 sides

rectangle = Rectangle("Square", 4)
rectangle.describe(type="square") # Square is a square rectangle with 4 sides