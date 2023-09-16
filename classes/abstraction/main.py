from abstraction_file import Circle, Rectangle

if __name__ == '__main__':
    # Creating objects
    circle = Circle(5)
    rectangle = Rectangle(4, 6)

    # Calling area method
    print(f"Circle Area: {circle.area()}")
    print(f"Rectangle Area: {rectangle.area()}")
