class Shape:
    def area(self, shape):
        if isinstance(shape, Rectangle):
            return shape.width * shape.height
        elif isinstance(shape, Circle):
            return 3.14 * (shape.radius ** 2)  # Not extensible
#--- Issue: The Shape class’s area method needs to be modified every time a new shape is added. 
# This tight coupling makes the code fragile and difficult to maintain.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)
    

#-- Improvement: By defining an abstract class Shape, you can extend it with new shapes like Rectangle and Circle, each implementing the area method. 
# You don’t need to modify existing code when adding new shapes, thus adhering to OCP.
