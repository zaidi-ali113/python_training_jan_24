from inheritance_file import Dog, Cat

if __name__ == '__main__':
    # Creating objects
    dog = Dog("Buddy")
    cat = Cat("Whiskers")

    # Calling subclass methods
    print(dog.speak())  # Output: Buddy says Woof!
    print(cat.speak())  # Output: Whiskers says Meow
