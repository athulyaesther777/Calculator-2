# Advanced Calculator

# Function to perform calculations
def calculate(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    elif operator == "**":
        return num1 ** num2
    elif operator == "%":
        return num1 % num2
    else:
        return "Invalid operator"

# Collect basic information from the user
num1 = float(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /, **, %): ")
num2 = float(input("Enter the second number: "))

# Perform calculation
result = calculate(num1, operator, num2)

# Print the result
print(f"Result: {result}")

# Examples of the output:
"""
Example 1:
Enter the first number: 56
Enter the operator: +
Enter the second number: 21
Result: 77.0

Example 2:
Enter the first number: 8
Enter the operator: /
Enter the second number: 7
Result: 1.1428571428571428

Example 3:
Enter the first number: 45
Enter the operator: *
Enter the second number: 32
Result: 1440.0

Example 4:
Enter the first number: 2
Enter the operator: **
Enter the second number: 3
Result: 8.0

Example 5:
Enter the first number: 75
Enter the operator: 2
Enter the second number: 9
Invalid operator

Example 6:
Enter the first number: 10
Enter the operator: %
Enter the second number: 3
Result: 1.0
"""
