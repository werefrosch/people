from random import randrange


class Person:
    def __init__(self, mother, father, place, name, death_rate):
        self.mother = mother
        self.father = father
        self.age = 0
        self.deceased = False
        self.name = name
        self.is_employed = False
        self.cash = 0
        self.occupation = place
        self.death_rate = death_rate

    def die(self):
        self.deceased = True

    def grow(self):
        if randrange(0, 99) == 0:
            if not self.is_employed:
                self.is_employed = True
            else:
                self.is_employed = False

        if self.is_employed:
            self.cash += randrange(1, 2)
        if not self.deceased:
            self.age += 1
        if randrange(0, round(self.death_rate*self.occupation.quality)) <= 1:
            self.die()
        if self.age >= 99:
            self.die()



