# polymorphism_demo.py

import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must override the area() method")

class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == "__main__":
    shapes = [
        Rectangle(5, 3),
        Circle(4)
    ]

    for shape in shapes:
        print(f"{shape.__class__.__name__} area: {shape.area():.2f}")

from polymorphism_demo import Shape, Rectangle, Circle
import math

def main():
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()