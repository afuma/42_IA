
import sys

def main():
    if (len(sys.argv) > 2):
        print("Assertion error: more than one argument are provided")
    if (len(sys.argv) > 1):
        nbr = 0
        arg = sys.argv[1]
        try:
            nbr = int(arg)
        except ValueError:
            print("Assertion error: argument is not an integer")
            return (0)
        if (nbr == 0):
            print("I'm Zero")
        elif (nbr % 2 == 0):
            print("I'm Even")
        elif (nbr % 2 == 1):
            print("I'm Odd")

main()
