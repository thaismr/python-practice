"""
OPERATORS OVERLOAD: Add functionality for default operators to work with our own objects
"""
from oop.myerror import RectComparisonError


class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_area(self):
        return self.x * self.y

    def __repr__(self):
        # what we get when printing a Rectangle object:
        return f"<class 'Rectangle({self.x}, {self.y})'>"

    def __add__(self, other):
        # what we get when using (+) operator with our object:
        if isinstance(other, Rectangle):
            x = self.x + other.x
            y = self.y + other.y
            return Rectangle(x, y)

        raise RectComparisonError('Cannot add Rectangle to type', type(other))

    def __eq__(self, other):
        # what to do for operator (==) between two Rectangles:
        if isinstance(other, Rectangle):
            return True if self.x == other.x and self.y == other.y else False

        raise RectComparisonError('Cannot compare Rectangle with type', type(other))

    def __lt__(self, other):
        # what to do for operator (<) less than (here we consider the area size):
        if isinstance(other, Rectangle):
            return True if self.get_area() < other.get_area() else False

        raise RectComparisonError('Cannot compare Rectangle with type', type(other))


rect1 = Rectangle(10, 20)
rect2 = Rectangle(10, 20)
rect3 = rect1 + rect2

print(rect1)
print(rect3)
print(rect1 == rect2)
print(rect1 > rect3)
