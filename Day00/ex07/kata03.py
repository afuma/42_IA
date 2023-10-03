kata = "The right format"

str_tirets = ""
nb_tirets = 42 - len(kata) - 1
for i in range(nb_tirets):
    str_tirets += '-'
print(str_tirets + kata)