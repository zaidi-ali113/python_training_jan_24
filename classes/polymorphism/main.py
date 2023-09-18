from polymorphism_file import Dog, Cat

if __name__ == '__main__':
    # Polymorphic behavior
    def animal_sound(animal):
        return animal.speak()


    # Creating objects
    dog = Dog()
    cat = Cat()

    # Calling the common function with different objects
    print(animal_sound(dog))  # Output: Woof!
    print(animal_sound(cat))  # Output: Meow!

