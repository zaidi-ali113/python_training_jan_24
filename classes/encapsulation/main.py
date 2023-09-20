from encapsulation_file import Dog, Cat

if __name__ == '__main__':
    # Creating objects
    dog = Dog("Buddy")
    cat = Cat("Whiskers")

    dog._species = "Canine"


    # Calling subclass methods
    print(dog.speak())  # Output: Buddy the Dog says Woof!
    print(cat.speak())  # Output: Whiskers the Cat says Meow!

    print(f"{dog.get_name()} is a {dog._species}.")
