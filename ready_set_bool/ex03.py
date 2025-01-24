import argparse

def  eval_formula(expression):
    # Mapping the symbols to Python equivalents
    logic_map = {
        "0": "False",  # Logical false
        "1": "True",   # Logical true
        "!": "not",    # Negation
        "&": "and",    # Conjunction (logical AND)
        "|": "or",     # Disjunction (logical OR)
        "^": "^",      # Exclusive disjunction (XOR)
        ">": "(not a or b)",  # Material condition (implication)
        "=": "=="      # Logical equivalence
    }

    # Check RPN validity (at least two logical expressions and one operator)
    operands = 0
    operators = 0
    for char in expression:
        if char.isalpha() or char in "01":
            operands += 1
        elif char in logic_map:
            operators += 1
    if (not any(op in expression for op in logic_map.keys() if op not in "01")) or (operands < 2 or operators < 1 or operands - operators != 1):
        print("Invalid RPN expression: it must contain at least two operands and one operator, and be well-formed.")
        return 1

    # Stack for evaluating the expression
    stack = []

    # Iterating through the expression in reverse order
    for char in expression:
        if char in "01":  # If it's a literal
            stack.append(logic_map[char])  # Push 'True' or 'False' to the stack
        elif char in "!&|^=":  # If it's an operator
            if char == "!":  # Negation is unary
                a = eval(stack.pop())
                stack.append(str(not a))
            else:  # Binary operators
                b = eval(stack.pop())
                a = eval(stack.pop())
                if char == "&":
                    stack.append(str(a and b))
                elif char == "|":
                    stack.append(str(a or b))
                elif char == "^":
                    stack.append(str(a ^ b))
                elif char == ">":
                    stack.append(str(not a or b))
                elif char == "=":
                    stack.append(str(a == b))


    # Final result is the last item in the stack
    return eval(stack.pop())

if __name__ == "__main__":
    # Initialize argument parser
    parser = argparse.ArgumentParser(description="Evaluate a logical expression using custom logic symbols.")

    # Add the argument for the logical expression
    parser.add_argument("expression", type=str, help="Logical expression to evaluate (e.g., '10&').")

    # Parse the arguments
    args = parser.parse_args()

    # Evaluate the logical expression
    result = eval_formula(args.expression)

    # Print the result
    if result != 1:
        print(f"{args.expression}: {result}")
