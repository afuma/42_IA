kata = (19,42,21)
string = ""
for nbr in kata:
    string = string + str(nbr) + ", "
string = string[:-2]
print("The " + str(len(kata)) + " numbers are: " + string)