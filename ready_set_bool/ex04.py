import argparse

def print_truth_table(expression):
    # Mapping the symbols to Python equivalents
    logic_map = {
        "0": "False",  # Logical false
        "1": "True",   # Logical true
        "!": "not",    # Negation (unary operator)
        "&": "and",    # Conjunction (logical AND)
        "|": "or",     # Disjunction (logical OR)
        "^": "^",      # Exclusive disjunction (XOR)
        ">": "(not a or b)",  # Material condition (implication)
        "=": "=="      # Logical equivalence
    }

    def evaluate_rpn(expression, values):
        stack = []
        for char in expression:
            if char.isalpha():
                stack.append(values[char.upper()])
            elif char in logic_map:
                if char == "!":
                    a = stack.pop()
                    stack.append(not a)
                else:
                    b = stack.pop()
                    a = stack.pop()
                    if char == "&":
                        stack.append(a and b)
                    elif char == "|":
                        stack.append(a or b)
                    elif char == "^":
                        stack.append(a ^ b)
                    elif char == ">":
                        stack.append(not a or b)
                    elif char == "=":
                        stack.append(a == b)
        return stack.pop()

    # Extract letters and normalize to uppercase
    letters = [char.upper() for char in expression if char.isalpha()]

    # Check RPN validity (at least one operand and correct number of operators)
    operands = 0
    operators = 0
    for char in expression:
        if char.isalpha() or char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            operands += 1
        elif char in logic_map:
            operators += 1
            if char == "!":
                operands -= 0  # Negation does not require an extra operand
            else:
                operands -= 1  # Binary operators require one less operand
    if operands != 1:
        print("Invalid RPN expression: it must contain a valid number of operands and operators, and be well-formed.")
        return
    # Check for duplicates
    if len(letters) != len(set(letters)):
        print("Duplicate letters found in the expression.")
        return

    # Print the count of unique letters
    unique_letter_count = len(set(letters))

    # Generate the table header
    table_head = '| ' + ' | '.join(letters) + ' | = |'
    print(table_head)
    separator = '|---' * len(letters) + '|---|'
    print(separator)

    # Generate the binary table and evaluate the expression
    for i in range(pow(2, unique_letter_count)):
        binary_row = f'{i:0{unique_letter_count}b}'  # Convert to binary with leading zeros
        values = {letters[j]: bool(int(binary_row[j])) for j in range(unique_letter_count)}
        result = evaluate_rpn(expression, values)
        formatted_row = '| ' + ' | '.join(binary_row) + f' | {int(result)} |'
        print(formatted_row)

if __name__ == "__main__":
    # Initialize argument parser
    parser = argparse.ArgumentParser(description="Generate and evaluate a truth table for a given logical RPN expression.")

    # Add the argument for the logical expression
    parser.add_argument("expression", type=str, help="Logical expression to evaluate (e.g., 'AB&', 'A!').")

    # Parse the arguments
    args = parser.parse_args()

    truth_table = print_truth_table(args.expression)
