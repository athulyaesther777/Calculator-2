# Advanced Calculator

# Collect basic information from the user
num1 = float(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

# Perform calculation based on the operator
if operator == "+":
    print(f"Result: {num1 + num2}")
elif operator == "-":
    print(f"Result: {num1 - num2}")
elif operator == "*":
    print(f"Result: {num1 * num2}")
elif operator == "/":
    # Check to avoid division by zero
    if num2 != 0:
        print(f"Result: {num1 / num2}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator")

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
Enter the first number: 75
Enter the operator: 2
Enter the second number: 9
Invalid operator
"""
