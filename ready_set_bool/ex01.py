import argparse
from ex00 import adder

def multiplier(a, b):
    result = 0

    # Handle negative numbers
    negative = False
    if a < 0:
        negative = not negative
        a = -a
    if b < 0:
        negative = not negative
        b = -b

    while b > 0:
        # Check if the least significant bit of b is 1
        if b & 1:
            result = adder(result, a)  # Add 'a' to result

        # Shift 'a' left by 1 (equivalent to multiplying by 2)
        a <<= 1

        # Shift 'b' right by 1 (equivalent to dividing by 2)
        b >>= 1

    return -result if negative else result

if __name__ == "__main__":
    # Argument parser
    parser = argparse.ArgumentParser(description="Perform multiplication using bitwise operators.")
    parser.add_argument("a", type=int, help="First integer to multiply")
    parser.add_argument("b", type=int, help="Second integer to multiply")
    args = parser.parse_args()

    # Multiply and print the result
    result = multiplier(args.a, args.b)
    print(f"The result of {args.a} * {args.b} is {result}")
