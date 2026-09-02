def add(a, b):
  return f'{a} + {b} = {a + b}'
  
def subtract(a, b):
  return f'{a} - {b} = {a - b}'
  
def multiply(a, b):
  return f'{a} * {b} = {a * b}'

def division(a, b):
    try:
        return f'{a} divided by {b} is {a / b}'
    except ZeroDivisionError:
        print("You can't divide a number by zero")

def average(a, b):
    return f'average of {a} and {b} is {sum(a + b) / 2}'
  
def modulus(a, b):
    return f'The remainder when {a} is divided by {b} is {a % b}'
