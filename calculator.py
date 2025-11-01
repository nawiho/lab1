# Calculator Functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a + b  # ОШИБКА: должно быть a * b

def divide(a, b):
    if b == 0:
        raise ValueError('Cannot divide by zero')
    return a / b

def power(a, b):
    return a ** b
