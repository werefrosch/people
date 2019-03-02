from random import randrange
from time import sleep
from Person import Person
from generators import generate_name


# ----------------------------------------------------------------
p = []
p.append(Person("Black", "White", "Creation", "God"))
p[0].deceased = True

for i in range(0, 10):
    p.append(Person(p[0], p[0], generate_name(), generate_name()))

alive = []
for i in range(len(p)):
    if not p[i].deceased:
        alive.append(i)


def randpers():
    j = randrange(len(alive))
    return p[alive[j]]


def procreate():
    par1 = randpers()
    par2 = randpers()
    occ = par1.occupation
    p.append(Person(par1, par2, occ, generate_name()))
    alive.append(len(p)-1)


while True:
    justdied = []
    for i in range(len(alive)):
        asd = alive[i]
        print(p[asd].name, end="\t")
        print("Age: ", end="")
        print(p[asd].age, end="\t\t")
        print("Occupation: ", end="")
        print(p[asd].occupation, end="\t\t")
        print("Mom: ", end="")
        print(p[asd].mother.name, end="\t")
        print("Dad: ", end="")
        print(p[asd].father.name, end="\t")
        print("Cash: ", end="")
        print(p[asd].cash, end="\n")
        p[asd].grow()
        if randrange(0, 99) == 0:
            procreate()
        if p[asd].deceased:
            justdied.append(asd)
#    for i in range(len(p)):
#        print(i, ": ", p[i].deceased, end=" ")
    print("\n Zivych: ", len(alive))
    print("\n Mrtvych: ", len(p) - len(alive))

    for i in range(len(justdied)):
        alive.pop(alive.index(justdied[i]))

#    print(alive)
    print("\n\nOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")

    if len(alive) == 0:
        sleep(0.5)
