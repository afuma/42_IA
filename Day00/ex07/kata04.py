kata = (0, 4, 132.42222, 10000, 12345.67)

def add_zero(nbr):
    if (nbr < 10):
        return ("0" + str(nbr))
    else:
        return (str(nbr))

def sci_number(nbr):
    return ("{:.2e}".format(nbr))

str_1 = "module_" + add_zero(kata[0])
str_2 = "ex_" + add_zero(kata[1]) + " : " + str(round(kata[2], 2))
str_3 = sci_number(kata[3])
str_4 = sci_number(kata[4])

string_format = str_1 + ", " + str_2 + ", " + str_3 + ", " + str_4
print(string_format)