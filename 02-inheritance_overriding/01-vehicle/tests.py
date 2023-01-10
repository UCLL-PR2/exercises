import unittest
from student import *

class TestVehicleExercise(unittest.TestCase):
    def setUp(self):
        self.vehicle1 = Vehicle("Toyota", "Corolla", 2020)
        self.car1 = Car("Toyota", "Corolla", 2020, 4)
        self.truck1 = Truck("Toyota", "Tacoma", 2020, "large")


    def test_create_vehicle(self):
        self.assertEqual(self.vehicle1.make, "Toyota")
        self.assertEqual(self.vehicle1.model, "Corolla")
        self.assertEqual(self.vehicle1.year, 2020)
        self.assertEqual(self.vehicle1.speed, 0)

    def test_vehicle_accelerate(self):
        self.assertEqual(self.vehicle1.speed, 0)
        vehicle.accelerate()
        self.assertEqual(self.vehicle1.speed, 10)
        vehicle.accelerate()
        self.assertEqual(self.vehicle1.speed, 20)

    def test_vehicle_brake(self):
        self.vehicle1.speed = 20
        self.vehicle1.brake()
        self.assertEqual(self.vehicle1.speed, 13)
        self.vehicle1.brake()
        self.assertEqual(self.vehicle1.speed, 6)

    def test_vehicle_honk(self):
        self.assertEqual(self.vehicle1.honk(), "HONK!")

    def test_create_car(self):
        self.assertEqual(self.car1.make, "Toyota")
        self.assertEqual(self.car1.model, "Corolla")
        self.assertEqual(self.car1.year, 2020)
        self.assertEqual(self.car1.speed, 0)
        self.assertEqual(self.car1.num_doors, 4)

    def test_car_honk(self):
        self.assertEqual(self.car1.honk(), "Beep beep!")

    def test_create_truck(self):
        self.assertEqual(self.truck1.make, "Toyota")
        self.assertEqual(self.truck1.model, "Tacoma")
        self.assertEqual(self.truck1.year, 2020)
        self.assertEqual(self.truck1.speed, 0)
        self.assertEqual(self.truck1.bed_size, "large")


if __name__ == "__main__":
    unittest.main()
    