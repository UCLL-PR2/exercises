import unittest
from student import *

class TestAnimalEnclosureAndZooAnimal(unittest.TestCase):
    def setUp(self):
        self.animal = Animal("Leo", "lion", 5)
        self.enclosure = Enclosure("Lion Enclosure", 3)
        self.zoo_animal = ZooAnimal("Max", "tiger", 7, "Tiger Enclosure", 2)

    def test_animal_make_sound(self):
        self.assertEqual(self.animal.make_sound(), "Grrrrrrrrrrrr")

    def test_enclosure_add_animal_success(self):
        result = self.enclosure.add_animal(self.animal)
        self.assertTrue(result)
        self.assertEqual(len(self.enclosure.animals), 1)

    def test_enclosure_add_animal_failure(self):
        self.enclosure.add_animal(self.animal)
        self.enclosure.add_animal(self.animal)
        self.enclosure.add_animal(self.animal)
        result = self.enclosure.add_animal(self.animal)
        self.assertFalse(result)
        self.assertEqual(len(self.enclosure.animals), 3)

    def test_enclosure_remove_animal_success(self):
        self.enclosure.add_animal(self.animal)
        result = self.enclosure.remove_animal(self.animal)
        self.assertTrue(result)
        self.assertEqual(len(self.enclosure.animals), 0)

    def test_enclosure_remove_animal_failure(self):
        result = self.enclosure.remove_animal(self.animal)
        self.assertFalse(result)
        self.assertEqual(len(self.enclosure.animals), 0)

    def test_zoo_animal_add_animal_success(self):
        result = self.zoo_animal.add_animal(self.animal)
        self.assertTrue(result)
        self.assertEqual(len(self.zoo_animal.animals), 1)

    def test_zoo_animal_add_animal_failure(self):
        self.zoo_animal.add_animal(self.animal)
        result = self.zoo_animal.add_animal(self.animal)
        self.assertFalse(result)
        self.assertEqual(len(self.zoo_animal.animals), 1)

    def test_zoo_animal_remove_animal_success(self):
        self.zoo_animal.add_animal(self.animal)
        result = self.zoo_animal.remove_animal(self.animal)
        self.assertTrue(result)
        self.assertEqual(len(self.zoo_animal.animals), 0)

    def test_zoo_animal_remove_animal_failure(self):
        result = self.zoo_animal.remove_animal(self.animal)
        self.assertFalse(result)
        self.assertEqual(len(self.zoo_animal.animals), 0)

    def test_zoo_animal_inherits_from_animal_and_enclosure(self):
        self.assertIsInstance(self.zoo_animal, Animal)
        self.assertIsInstance(self.zoo_animal, Enclosure)

if __name__ == '__main__':
    unittest.main()

