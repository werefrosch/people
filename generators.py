from random import randrange

def generate_name():
    samo = "aeiou"
    spolu = "bcdfghjklmnpqrstvwxyz"
    name = samo[randrange(0, len(samo))] + spolu[randrange(0, len(spolu))]
    for ii in range(0, randrange(1, 3)):
        name += samo[randrange(0, len(samo))] + spolu[randrange(0, len(spolu))]
    name = name.capitalize()
    return name
