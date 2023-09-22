from custom_exception_file import SpecialDivideByZeroException

def divide(a, b):
    if b == 0:
        raise SpecialDivideByZeroException()
    return a / b

try:
    result = divide(10, 1)
    print(result)
except SpecialDivideByZeroException as e:
    print("Custom Exception:", e)
