from random import randint, random


class Zombie:
    """Zombie Class"""

    def __init__(self, speed, infection_rate):
        """Constructor for Zombie
        <speed>, <infection_rate>
        """
        self.speed = speed
        self.x = randint(0, 200)
        self.y = randint(0, 200)
        if random() < infection_rate:
            self.infected = True
        elif randint(1, 100) == 76:
            self.infected = False
        else:
            self.infected = False

    def touching(self, zombie):
        """sees if zombie is touching another
        <other_zombie>"""
        if 5 > self.x - zombie.x > -5 and 5 > self.y - zombie.y > -5:
            return True

    def move(self):
        """makes class move and change direction if against wall"""
        if 0 > self.x + self.speed > 200:
            self.speed = - self.speed
            self.x = self.x + self.speed
        else:
            self.x = self.x + self.speed

        if 0 > self.y + self.speed > 200:
            self.speed = - self.speed
            self.y = self.y + self.speed
        else:
            self.y = self.y + self.speed

    def infect(self):
        """turns zombie to infected"""
        if not self.infected:
            self.infected = True

    @property
    def is_infected(self):
        """returns T/F if infected"""
        return self.infected


class Doctor(Zombie):
    """Doctor class inherited from zombie"""
    def __init__(self, speed, infection_rate, healing_rate):
        """Constructor for doctor
        <speed>, <infection_rate> (0), <healing_rate>(1)"""
        Zombie.__init__(self, speed, infection_rate)
        self.infection_rate = 0
        self.speed = speed
        self.healing_rate = healing_rate
        self.x = randint(0, 200)
        self.y = randint(0, 200)

    def heal(self, infected_person):
        """method to heal an infected person"""
        infected_person.is_infected = False


class World:
    """world class"""

    def __init__(self):
        """constructor for world"""
        self.objectList = []
        self.doctorList = []

    def populate_world(self, population, initial_infection_rate):
        """method to populate the world
        <population>, <initial_infection_rate>"""
        for person in range(population):
            self.objectList.append(Zombie(2, initial_infection_rate))
        for j in range(1, 20):
            self.doctorList.append(Doctor(30, 0, 1))

    def update_world(self):
        """method to update the world"""
        for person in self.objectList:
            person.move()
            for other_zombie in self.objectList:
                if other_zombie.is_infected and person.touching(other_zombie):
                    person.infect()
            for other_zombie in self.objectList:
                if other_zombie.is_infected and other_zombie.touching(Doctor):
                    Doctor.heal(other_zombie)

    def get_number_infected(self):
        """get the number of infected people in the population"""
        num_infected = 0
        for infected in range(len(self.objectList)):
            if self.objectList[infected].infected:
                num_infected = num_infected + 1
        return num_infected

    def get_number_well(self):
        """get number of people no infected in the population"""
        num_well = 0
        for well in range(len(self.objectList)):
            if not self.objectList[well].infected:
                num_well = num_well + 1
        return num_well


if __name__ == '__main__':
    """Entry point to program"""
    moves = 10000
    my_world = World()
    my_world.populate_world(500, 0.4)
    for i in range(moves):
        my_world.update_world()
        print("Number infected:", my_world.get_number_infected())
        print("Number well:", my_world.get_number_well())
        if my_world.get_number_well() == 0:
            break



