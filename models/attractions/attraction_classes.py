class PettingZoo:

    def __init__(self, attraction_name, description):
        self.attraction_name = attraction_name
        self.description = description
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)

    def __str__(self):
        string = f"{self.attraction_name} is where you'll find {self.description}, like"
        for animal in self.animals:
            string += f'\n * {animal.name} the {animal.species}'
        return string


class SnakePit:

    def __init__(self, attraction_name, desscription):
        self.attraction_name = attraction_name
        self.description = desscription
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)

    def __str__(self):
        string = f"{self.attraction_name} is where you'll find {self.description}, like"
        for animal in self.animals:
            string += f'\n * {animal.name} the {animal.species}'
        return string


class Wetlands:

    def __init__(self, attraction_name, description):
        self.attraction_name = attraction_name
        self.description = description
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)

    def __str__(self):
        string = f"{self.attraction_name} is where you'll find {self.description}, like"
        for animal in self.animals:
            string += f'\n * {animal.name} the {animal.species}'
        return string
