class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def make_sound(self):
        return "Rrrrrrrrrrrr"

class Enclosure:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.animals = []

    def add_animal(self, animal):
        if len(self.animals) < self.capacity:
            self.animals.append(animal)
            return True
        else:
            return False

    def remove_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)
            return True
        else:
            return False

# Implement the ZooAnimal class here