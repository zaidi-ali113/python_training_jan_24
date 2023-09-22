class SpecialDivideByZeroException(Exception):
    def __init__(self):
        super().__init__("Divide by zero na ho payega")
