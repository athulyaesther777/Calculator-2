import re


def evaluate_expression(expression):
    try:
        # Use eval to evaluate the expressions
        # Security note: eval is dangerous if used with untrusted input
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except Exception as e:
        return f"Error: Invalid expression ({str(e)})."


def get_user_input():
    expression = input("Enter a mathematical expression (e.g., 3 + 4 * 2 / (1 - 5) ** 2 ** 3): ")
    return expression


def main():
    print("Advanced Calculator")
    print("You can use operators +, -, *, /, **, %, and parentheses for order of operations.")
    while True:
        expression = get_user_input()
        result = evaluate_expression(expression)
        print(f"Result: {result}")

        again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if again != 'yes':
            break
    print("Thank you for using the Advanced Calculator. Goodbye!")


if __name__ == "__main__":
    main()

# Examples of the output:
"""
Example 1:
Enter a mathematical expression (e.g., 3 + 4 * 2 / (1 - 5) ** 2 ** 3): 3 + 4 * 2
Result: 11.0

Example 2:
Enter a mathematical expression (e.g., 3 + 4 * 2 / (1 - 5) ** 2 ** 3): 3 + 4 * 2 / (1 - 5) ** 2
Result: 3.5

Example 3:
Enter a mathematical expression (e.g., 3 + 4 * 2 / (1 - 5) ** 2 ** 3): 10 % 3
Result: 1

Example 4:
Enter a mathematical expression (e.g., 3 + 4 * 2 / (1 - 5) ** 2 ** 3): 2 ** 3 ** 2
Result: 512

Example 5:
Enter a mathematical expression (e.g., 3 + 4 * 2 / (1 - 5) ** 2 ** 3): 10 / 0
Result: Error: Division by zero is not allowed.

Example 6:
Enter a mathematical expression (e.g., 3 + 4 * 2 / (1 - 5) ** 2 ** 3): 5 + 2 *
Result: Error: Invalid expression (unexpected EOF while parsing (<string>, line 1)).
"""
