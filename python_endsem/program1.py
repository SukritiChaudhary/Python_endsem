# Make a zero division error handler with built in exceptions.
num1 = int(input("Enter numerator: "))
num2 = 0

try:
    result = num1 / num2
    print(f"The result of {num1} / 0 is {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")