import argparse

def gray_code(a):
    """
    Converts a number to its Gray code equivalent.
    Gray code is calculated as a XOR (a >> 1).
    """
    return a ^ (a >> 1)

if __name__ == "__main__":
    # Initialize argument parser
    parser = argparse.ArgumentParser(description="Convert a number to its Gray code equivalent.")

    # Add the argument for the input number
    parser.add_argument("a", type=int, help="The integer to convert to Gray code.")

    # Parse the arguments
    args = parser.parse_args()

    # Calculate the Gray code
    result = gray_code(args.a)

    # Print the result
    print(f"The Gray code for {args.a} is {result}")
