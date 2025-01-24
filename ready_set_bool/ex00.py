import argparse

def adder(a, b):
    while b != 0:
        # Calculate the carry
        carry = a & b

        # Calculate the sum without the carry
        a = a ^ b

        # Shift the carry to the left
        b = carry << 1
    return a

if __name__ == "__main__":
    # Initialize the argument parser
    parser = argparse.ArgumentParser(description="Perform addition using bitwise operators.")

    # Add arguments for the two parameters
    parser.add_argument("a", type=int, help="First integer to add")
    parser.add_argument("b", type=int, help="Second integer to add")

    # Parse the arguments
    args = parser.parse_args()

    # Call the add function with parsed arguments
    result = adder(args.a, args.b)

    # Print the result
    print(f"The result of {args.a} + {args.b} is {result}")
