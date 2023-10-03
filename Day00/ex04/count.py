import sys
import re

def text_analyzer(string=""):
    '''
    This function counts the number of upper characters, lower characters,\r
    punctuation and spaces in a given text.
    '''
    if (string == ''):
        print("What is the text to analyze ?")
        string = input(">> ")
        print(string)
    if (isinstance(string, str)):
        print("The text contains " + str(len(string)) + " character(s):")
        nb_maj = len(re.findall("[A-Z]", string))
        print("- " + str(nb_maj) + " upper letter(s)")
        nb_min = len(re.findall("[a-z]", string))
        print("- " + str(nb_min) + " lower letter(s)")
        punct_marks = len(re.findall("[:,;?!.\-']", string))
        print("- " + str(punct_marks) + " punctuation mark(s)")
        spaces = len(re.findall(" ", string))
        print("- " + str(spaces) + " space(s)")
    else:
        print("AssertionError: argument is not a string")

string = "Python 2.0, released 2000, introduced features like List comprehensions \
    and a garbage collection system capable of collecting reference cycles."
# text_analyser(string)

if (__name__ == "__main__"):
	if(len(sys.argv) == 2):
		text_analyzer(sys.argv[1])
	else:
		print("AssertionError: one argument is needed")
