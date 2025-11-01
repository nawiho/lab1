def square(x):
    return x * x

def cube(x):
    return x * x * x

def square_root(x):
    if x < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return x ** 0.5

def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b
