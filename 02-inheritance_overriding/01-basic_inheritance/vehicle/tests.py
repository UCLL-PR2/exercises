import unittest
from student import *

class TestCarAndElectricCar(unittest.TestCase):
    def setUp(self):
        self.car = Car("Toyota", "Camry", 2021)
        self.electric_car = ElectricCar("Tesla", "Model S", 2022, 85)

    def test_car_description(self):
        self.assertEqual(self.car.description(), "Toyota Camry (2021)")

    def test_electric_car_description(self):
        self.assertEqual(self.electric_car.description(), "Tesla Model S (2022)")

    def test_electric_car_range_60(self):
        electric_car_60 = ElectricCar("Tesla", "Model 3", 2023, 60)
        self.assertEqual(electric_car_60.range(), 140)

    def test_electric_car_range_85(self):
        self.assertEqual(self.electric_car.range(), 240)

    def test_electric_car_range_unknown(self):
        electric_car_unknown = ElectricCar("Tesla", "Model X", 2023, 100)
        self.assertEqual(electric_car_unknown.range(), "Range not available for this battery size.")

    def test_electric_car_inherits_from_car(self):
        self.assertIsInstance(self.electric_car, Car)

if __name__ == '__main__':
    unittest.main()
