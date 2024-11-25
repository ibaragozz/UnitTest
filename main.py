def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def check(number):
    return number % 2 == 0

def divide(a, b):
    if b == 0:
        raise ValueError('Cannot divide by zero')
    return a / b

# Домашнее задание

def hw(a, b):
    if b == 0:
        raise ValueError('Cannot divide by zero')
    return a % b