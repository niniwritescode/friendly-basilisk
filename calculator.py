
# Simple Calculator in Python

# Ask the user to enter two numbers
a = float(input("Enter the first number:"))
b = float(input("Enter the second number:  "))

# Ask the user to choose an operation
print("Choose an operation: +, -, *, /")
operation = input("Enter the operation: ")

# Perform the calculation based on the chosen operation
if operation == "+":
    result = a + b
elif operation == "-":
    result = a - b
elif operation == "*":
    result = a * b
elif operation == "/":
    if b != 0:
        result = a / b
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation."

# Show the result
print("Result:", result)
