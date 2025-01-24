import argparse

def parse_rpn_to_tree(expression):
    """
    Parses an RPN (Reverse Polish Notation) expression into a nested tuple structure.
    Returns a single root node that represents the entire parse tree.
    """
    stack = []
    variables_seen = set()

    for char in expression:
        if char.isalpha():
            if char in variables_seen:
                raise ValueError("Duplicate letters found in the expression.")
            variables_seen.add(char)
            stack.append(("var", char))   # e.g. ("var", "A")
        elif char in ("&", "|", "^", ">", "="):
            # It's a binary operator; pop two nodes
            if len(stack) < 2:
                raise ValueError(f"Not enough operands on stack.")
            right = stack.pop()
            left = stack.pop()
            # e.g. ("op", "&", ("var","A"), ("var","B"))
            stack.append(("op", char, left, right))
        elif char == "!":
            # It's a unary operator (negation); pop one node
            if len(stack) < 1:
                raise ValueError(f"Not enough operands on stack for operator '!'")
            child = stack.pop()
            # e.g. ("not", ("var","A"))
            stack.append(("not", child))
        else:
            raise ValueError(f"Invalid character in expression: '{char}'")

    if len(stack) != 1:
        raise ValueError("Invalid RPN expression: it must form exactly one complete expression.")

    return stack[0]


def nnf_transform(node):
    """
    Convert the parse tree into Negation Normal Form (NNF),
    where all negations are pushed down and double negation is removed.
    """
    node_type = node[0]

    # Case 1: Variable node
    if node_type == "var":
        return node  # Already in NNF

    # Case 2: Operator node
    elif node_type == "op":
        op = node[1]
        left = node[2]
        right = node[3]
        left_nnf = nnf_transform(left)
        right_nnf = nnf_transform(right)

        # A > B => !A | B
        if op == ">":
            not_left = nnf_transform(("not", left_nnf))
            return nnf_transform(("op", "|", not_left, right_nnf))

        # A = B => (A & B) | (!A & !B)
        elif op == "=":
            not_left = nnf_transform(("not", left_nnf))
            not_right = nnf_transform(("not", right_nnf))
            return nnf_transform((
                "op", "|",
                ("op", "&", left_nnf, right_nnf),
                ("op", "&", not_left, not_right)
            ))

        # Handle AND, OR, XOR
        else:
            return ("op", op, left_nnf, right_nnf)

    # Case 3: Negation node
    elif node_type == "not":
        child = nnf_transform(node[1])

        # Remove double negation !!A -> A
        if child[0] == "not":
            return nnf_transform(child[1])

        # If child is a variable, simply add negation to it
        if child[0] == "var":
            if child[1].endswith("!"):  # Handle existing negation
                return ("var", child[1][:-1])  # Remove extra negation
            return ("var", child[1] + "!")  # Add negation

        # Apply De Morgan's laws if negating an operator
        if child[0] == "op":
            op = child[1]
            left = child[2]
            right = child[3]

            if op == "&":
                # !(A & B) => !A | !B
                return nnf_transform((
                    "op", "|",
                    ("not", left),
                    ("not", right)
                ))
            elif op == "|":
                # !(A | B) => !A & !B
                return nnf_transform((
                    "op", "&",
                    ("not", left),
                    ("not", right)
                ))
            elif op == "^":
                # !(A ^ B) => A = B
                return nnf_transform(("op", "=", left, right))
            elif op == ">":
                # !(A > B) => A & !B
                return nnf_transform(("op", "&", left, ("not", right)))
            elif op == "=":
                # !(A = B) => A ^ B
                return nnf_transform(("op", "^", left, right))

        raise ValueError("Unexpected structure when applying negation.")

    else:
        raise ValueError("Unknown node type encountered during NNF transformation.")


def tree_to_rpn(node):
    """
    Converts the (already NNF-transformed) tree back into an RPN string.
    """
    node_type = node[0]

    # Variable node, e.g. ("var", "A") or ("var", "A!")
    if node_type == "var":
        return node[1]

    # Operator node, e.g. ("op", "&", left, right)
    elif node_type == "op":
        op = node[1]
        left = node[2]
        right = node[3]
        return tree_to_rpn(left) + tree_to_rpn(right) + op

    # We should never see a "not" node in final NNF form
    elif node_type == "not":
        # If it happens, it's an error in the transformation logic
        raise ValueError("Unexpected 'not' node in final NNF tree.")

    else:
        raise ValueError("Unknown node type in tree_to_rpn.")


def negation_normal_form(expression):
    """
    Main function that:
      1) Parses the RPN expression into a tuple-based tree.
      2) Transforms that tree into NNF (pushing negations down).
      3) Returns the final expression in RPN form.
    """
    root = parse_rpn_to_tree(expression)
    nnf_root = nnf_transform(root)
    return tree_to_rpn(nnf_root)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate a negation logical expression in RPN and convert to NNF.")
    parser.add_argument("expression", type=str, help="Logical expression in RPN (e.g., 'AB&!').")
    args = parser.parse_args()

    try:
        result = negation_normal_form(args.expression)
        print(result.upper())
    except ValueError as e:
        print(f"Error: {e}")
