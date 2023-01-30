import unittest
from student import *

class TestAnimalInheritance(unittest.TestCase):
    def setUp(self):
        self.animal = Animal("Fluffy", "Cat")
        self.dog1 = Dog("Rover", "Labrador")
        self.dog2 = Dog("Fido", "Poodle")
        self.cat1 = Cat("Fluffy", "Siamese")
        self.parrot1 = Parrot("Polly", "African Grey")
        self.fish1 = Fish("Goldie", "Goldfish")
        self.petshop = PetShop("Paws and Claws")
        self.petshop.add_animal(self.dog1)
        self.petshop.add_animal(self.dog2)
        self.petshop.add_animal(self.cat1)
        self.petshop.add_animal(self.parrot1)
        self.petshop.add_animal(self.fish1)

    def test_create_animal(self):
        self.assertEqual(self.animal.name, "Fluffy")
        self.assertEqual(self.animal.species, "Cat")
        self.assertEqual(self.animal.make_sound(), "Some generic animal sound")

    def test_create_dog(self):
        self.assertEqual(self.dog1.name, "Rover")
        self.assertEqual(self.dog1.species, "Dog")
        self.assertEqual(self.dog1.breed, "Labrador")
        self.assertEqual(self.dog1.make_sound(), "Bark")

    def test_create_cat(self):
        self.assertEqual(self.cat1.name, "Fluffy")
        self.assertEqual(self.cat1.species, "Cat")
        self.assertEqual(self.cat1.breed, "Siamese")
        self.assertEqual(self.cat1.make_sound(), "Meow")

    def test_create_parrot(self):
        self.assertEqual(self.parrot1.name, "Polly")
        self.assertEqual(self.parrot1.species, "Parrot")
        self.assertEqual(self.parrot1.breed, "African Grey")
        self.assertEqual(self.parrot1.make_sound(), "Squawk")

    def test_create_fish(self):
        self.assertEqual(self.fish1.name, "Goldie")
        self.assertEqual(self.fish1.species, "Fish")
        self.assertEqual(self.fish1.breed, "Goldfish")
        self.assertEqual(self.fish1.make_sound(), "Bubble bubble")

    def test_pet_shop(self):
        self.assertEqual(self.petshop.name, "Paws and Claws")
        self.assertEqual(len(self.petshop.animals), 5)
        self.petshop.sell_animal(self.dog1)
        self.assertEqual(len(self.petshop.animals), 4)

    def test_sell_animal(self):
        # Test selling an animal that's in the pet shop
        self.petshop.sell_animal(self.dog1)
        self.assertNotIn(self.dog1, self.petshop.animals)
        
        # Test selling an animal that's not in the pet shop
        with self.assertRaises(ValueError) as context:
            self.petshop.sell_animal(self.dog1)
        self.assertEqual(str(context.exception), "This animal is not available!")
        
        # Test selling a non-animal object
        with self.assertRaises(TypeError) as context:
            self.petshop.sell_animal("Not an animal")
        self.assertEqual(str(context.exception), "The object is not of type 'Animal'")

if __name__ == "__main__":
    unittest.main()
