def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

def modulus(x, y):
    return x % y

def exponent(x, y):
    return x ** y

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /, %, **): ")

result = 0
if operation == '+':
    result = add(num1, num2)
elif operation == '-':
    result = subtract(num1, num2)
elif operation == '*':
    result = multiply(num1, num2)
elif operation == '/':
    result = divide(num1, num2)
elif operation == '%':
    result = modulus(num1, num2)
elif operation == '**':
    result = exponent(num1, num2)
else:
    print("Invalid operation!")

print(f"Result: {result}")
