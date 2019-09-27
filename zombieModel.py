from random import randint, random


class Zombie:
    """"""

    def __init__(self, speed, infection_rate):
        """Constructor for Zombie"""
        self.speed = speed
        self.x = randint(0, 200)
        self.y = randint(0, 200)
        if random < infection_rate:
            self.infected = True
        else:
            self.infected = False

    def touching(self, zombie: Zombie):
        if self.x == zombie.x and self.y == zombie.y
            return True

    def move(self):
        self.x = self.x + self.speed
        self.y = self.y + self.speed

    def infect(self):
        if not self.infected:
            self.infected = True


class World():
    """"""

    def __init__(self, ):
        self.objectList = []

    def populate_world(self, population):
        for person in population:
            self.objectList.append(Zombie(2))

    def update_world(self):
        for person in self.objectList:
            person.move()
