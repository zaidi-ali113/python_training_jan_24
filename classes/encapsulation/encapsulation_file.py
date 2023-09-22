class Animal:
    def __init__(self, name):
        self.__name = name  # Private variable
        self._species = "Unknown"  # Protected variable

    def speak(self):
        pass  # Base class method

    def get_name(self):  # Accessor for private variable
        return self.__name


class Dog(Animal):
    def speak(self):
        return f"{self.get_name()} the Dog says Woof!"  # Accessing private variable via accessor


class Cat(Animal):
    def speak(self):
        return f"{self.get_name()} the Cat says Meow!"
