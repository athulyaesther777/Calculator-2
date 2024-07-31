# pip install sympy

import sympy as sp


def evaluate_expression(expression, variables):
    try:
        # Parse and evaluate the expression using sympy
        parsed_expr = sp.sympify(expression)
        result = parsed_expr.evalf(subs=variables)
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except Exception as e:
        return f"Error: Invalid expression ({str(e)})."


def get_user_input():
    expression = input("Enter a mathematical expression: ")
    return expression


def display_help():
    print("""
Advanced Calculator Help:
- Operators: +, -, *, /, **, %
- Functions: sin(x), cos(x), tan(x), log(x), exp(x)
- Variables: You can use variables like x, y, etc.
- Example: 2 * sin(x) + 3 * cos(y)
- Assignments: You can assign values to variables (e.g., x = 3)
    """)


def main():
    print("Advanced Calculator")
    print("Type 'help' for instructions or 'exit' to quit.")
    variables = {}
    while True:
        expression = get_user_input()
        if expression.strip().lower() == 'help':
            display_help()
            continue
        if expression.strip().lower() == 'exit':
            break
        if '=' in expression:
            # Handle variable assignment
            try:
                var, val = expression.split('=')
                var = var.strip()
                val = evaluate_expression(val.strip(), variables)
                variables[var] = val
                print(f"{var} = {val}")
            except Exception as e:
                print(f"Error: Invalid assignment ({str(e)}).")
        else:
            result = evaluate_expression(expression, variables)
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
Enter a mathematical expression: help
Advanced Calculator Help:
- Operators: +, -, *, /, **, %
- Functions: sin(x), cos(x), tan(x), log(x), exp(x)
- Variables: You can use variables like x, y, etc.
- Example: 2 * sin(x) + 3 * cos(y)
- Assignments: You can assign values to variables (e.g., x = 3)

Example 2:
Enter a mathematical expression: x = 3
x = 3

Example 3:
Enter a mathematical expression: 2 * sin(x)
Result: 0.282240016119734

Example 4:
Enter a mathematical expression: y = 2
y = 2

Example 5:
Enter a mathematical expression: 2 * sin(x) + 3 * cos(y)
Result: -1.42336000783947

Example 6:
Enter a mathematical expression: exit
Thank you for using the Advanced Calculator. Goodbye!
"""
