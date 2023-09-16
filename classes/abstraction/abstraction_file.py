from abc import ABC, abstractmethod

# Abstract class with abstract method
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Concrete subclasses
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
