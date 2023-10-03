
import sys
import re

def main(s, n):
    try:
        n = int(n)
    except ValueError:
        print("AssertionError: second arguments integers")
        return 
    if (not isinstance(s, str)):
        print("ERROR")
        return
    filter_words = []
    s = re.sub("[:,;?!.\-']", " ", s)
    split_words = s.split()
    for word in split_words:
        if (len(word) > n):
            filter_words.append(word)
    return (filter_words)

if (__name__ == "__main__"):
    if (len(sys.argv) > 3):
        print("Too much arguments !")
    elif (len(sys.argv) < 2):
        print("No argument passed !")
    elif (len(sys.argv) == 2):
        print("Second argument missed !")
    else:
        filter_words = main(sys.argv[1], sys.argv[2])
        if(filter_words is not None):
            print(filter_words)