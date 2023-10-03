kata = (2019, 9, 25, 3, 30)

def add_zero(nbr):
    if (nbr < 10):
        return ("0" + str(nbr))
    else:
        return (str(nbr))

date = f"{add_zero(kata[1])}/{add_zero(kata[2])}/{kata[0]}"
hour = f"{add_zero(kata[3])}:{add_zero(kata[4])}"
string_format = date + " " + hour
print(string_format)