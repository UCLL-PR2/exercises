import unittest
from app import *

class TestAnimalInheritance(unittest.TestCase):
    def test_create_animal(self):
        animal = Animal("Fluffy", "Cat")
        self.assertEqual(animal.name, "Fluffy")
        self.assertEqual(animal.species, "Cat")
        self.assertEqual(animal.make_sound(), "Some generic animal sound")

    def test_create_dog(self):
        dog = Dog("Rover", "Labrador")
        self.assertEqual(dog.name, "Rover")
        self.assertEqual(dog.species, "Dog")
        self.assertEqual(dog.breed, "Labrador")
        self.assertEqual(dog.make_sound(), "Bark")

    def test_create_cat(self):
        cat = Cat("Fluffy", "Siamese")
        self.assertEqual(cat.name, "Fluffy")
        self.assertEqual(cat.species, "Cat")
        self.assertEqual(cat.breed, "Siamese")
        self.assertEqual(cat.make_sound(), "Meow")

    def test_create_parrot(self):
        parrot = Parrot("Polly", "African Grey")
        self.assertEqual(parrot.name, "Polly")
        self.assertEqual(parrot.species, "Parrot")
        self.assertEqual(parrot.breed, "African Grey")
        self.assertEqual(parrot.make_sound(), "Squawk")

    def test_create_fish(self):
        fish = Fish("Goldie", "Goldfish")
        self.assertEqual(fish.name, "Goldie")
        self.assertEqual(fish.species, "Fish")
        self.assertEqual(fish.breed, "Goldfish")
        self.assertEqual(fish.make_sound(), "Bubble bubble")

    def test_pet_shop(self):
        petshop = PetShop("Paws and Claws")
        dog1 = Dog("Rover", "Labrador")
        dog2 = Dog("Fido", "Poodle")
        cat1 = Cat("Fluffy", "Siamese")
        parrot1 = Parrot("Polly", "African Grey")
        fish1 = Fish("Goldie", "Goldfish")
        petshop.add_animal(dog1)
        petshop.add_animal(dog2)
        petshop.add_animal(cat1)
        petshop.add_animal(parrot1)
        petshop.add_animal(fish1)
        self.assertEqual(petshop.name, "Paws and Claws")
        self.assertEqual(len(petshop.animals), 5)
        petshop.sell_animal(dog1)
        self.assertEqual(len(petshop.animals), 4)

if __name__ == "__main__":
    unittest.main()
