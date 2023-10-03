
import sys

def rev_string(string):
    return (string[::-1])

def rev_case(string):
    rev_string = ""
    for c in string:
        if(c.isupper()): rev_string += c.lower()
        elif(c.islower()): rev_string += c.upper()
        else: rev_string += " "
    return (rev_string)

def main():
    if (len(sys.argv) > 1):
        string = sys.argv[1]
        for arg in sys.argv[2:]:
            string = string + " " + arg
        print(rev_string(rev_case(string)))

main()