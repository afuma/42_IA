
import sys

def main():
    if (len(sys.argv) < 3):
        print("Usage: python operations.py <number1> <number2>")
        print("Example:")
        print("\tpython operations.py 10 3")
        return (0)
    if (len(sys.argv) > 3):
        print("AssertionError: More than one argument is provided")
        return (0)
    nbr1 = sys.argv[1]
    nbr2 = sys.argv[2]
    try:
        nbr1 = int(nbr1)
        nbr2 = int(nbr2)
    except ValueError:
        print("AssertionError: only integers")
    print("sum: ", nbr1 + nbr2)
    print("Difference: ", nbr1 - nbr2)
    print("Product: ", nbr1 * nbr2)
    try:
        print("Quotient: ", nbr1 / nbr2)
    except ZeroDivisionError:
        print("ERROR: (division by zero)")
    try:
        print("Remainder: ", nbr1 % nbr2)
    except ZeroDivisionError:
        print("ERROR: (modulo by zero)")

main()
