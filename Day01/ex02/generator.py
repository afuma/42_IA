
def shuffle(liste):
    n = len(liste)

    for i in range(0,n-1):
        pos = randint(i+1,n-1)
        liste[pos],liste[i] = liste[i],liste[pos]
    return (liste)

def generator(text, sep=" ", option=None):
    liste = text.split(" ")
    if (option != None):
        if (option == "shuffle"):
            liste = shuffle(liste)
        elif (option == "unique"):
            liste = list(set(liste))
        elif (option == "ordered"):
            liste.sort(reverse=True)
    

