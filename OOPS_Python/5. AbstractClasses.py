from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Method to calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Method to calculate the perimeter of the shape."""
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Usage
shapes = [Rectangle(3, 4), Circle(5)]

for shape in shapes:
    print(f'Area: {shape.area()}')
    print(f'Perimeter: {shape.perimeter()}')
