from random import randrange, random
from time import sleep
from Person import Person
from generators import generate_name
from Location import Location

poc_miest = 10
poc_ludi = 10
birth_rate = 99
death_rate = 99
moving_rate = 50

# PLACES ----------------------------------------------------------------


plc = []
for i in range(poc_miest):
    plc.append(Location(generate_name(), random()))

plc[1].name = "HELL"
plc[1].quality = 0.01

# PEOPLE ----------------------------------------------------------------
p = [Person("Black", "White", "Creation", "God", 1)]
p[0].deceased = True

for i in range(0, poc_ludi):
    p.append(Person(p[0], p[0], plc[randrange(len(plc))], generate_name(), death_rate))

alive = []
for i in range(len(p)):
    if not p[i].deceased:
        alive.append(i)


def rand_pers():
    j = randrange(len(alive))
    return p[alive[j]]


def procreate():
    par1 = rand_pers()
    par2 = rand_pers()
    occ = par1.occupation
    p.append(Person(par1, par2, occ, generate_name(), death_rate))
    alive.append(len(p)-1)


generation = 0

while True:
    justdied = []
    justmoved = []
    generation += 1
    for i in range(len(alive)):
        asd = alive[i]
        print(p[asd].name, end="\t")
        print("Age: ", end="")
        print(p[asd].age, end="\t\t")
        print("Occupation: ", end="")
        print(p[asd].occupation.name, end="\t\t")
        print("Mom: ", end="")
        print(p[asd].mother.name, end="\t")
        print("Dad: ", end="")
        print(p[asd].father.name, end="\t")
        print("Cash: ", end="")
        print(p[asd].cash, end="\n")
        p[asd].grow()
        if randrange(moving_rate) == 0:
            p[asd].occupation = plc[randrange(len(plc))]
            justmoved.append(asd)
        if randrange(birth_rate) == 0:
            procreate()
        if p[asd].deceased:
            justdied.append(asd)

    # TESTY ----------------------------------------------------------------
    if len(alive) << 2:
        procreate()
    for i in range(len(justdied)):
        alive.pop(alive.index(justdied[i]))

    # VYSTUP ----------------------------------------------------------------
    print("\nJust died: ", end="")
    for i in range(len(justdied)):
        print(p[justdied[i]].name, end=", ")
    print("\nJust moved: ", end="")
    for i in range(len(justmoved)):
        print(p[justmoved[i]].name, end=", ")

    print("\n\nZivych: ", len(alive) - 1)
    print("Mrtvych: ", len(p) - len(alive) - 1)
    print("Rok: ", generation)

    print("\n\n----------------------------------------------------------------------------------------------------")
#    sleep(0.01)

