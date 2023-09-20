from abc import ABC

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass  # Base class method

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"