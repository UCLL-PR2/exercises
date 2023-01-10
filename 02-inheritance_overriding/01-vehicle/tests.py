import unittest
from app import *

class TestVehicleExercise(unittest.TestCase):
    def test_create_vehicle(self):
        vehicle = Vehicle("Toyota", "Corolla", 2020)
        self.assertEqual(vehicle.make, "Toyota")
        self.assertEqual(vehicle.model, "Corolla")
        self.assertEqual(vehicle.year, 2020)
        self.assertEqual(vehicle.speed, 0)

    def test_vehicle_accelerate(self):
        vehicle = Vehicle("Toyota", "Corolla", 2020)
        self.assertEqual(vehicle.speed, 0)
        vehicle.accelerate()
        self.assertEqual(vehicle.speed, 10)
        vehicle.accelerate()
        self.assertEqual(vehicle.speed, 20)

    def test_vehicle_brake(self):
        vehicle = Vehicle("Toyota", "Corolla", 2020)
        vehicle.speed = 20
        vehicle.brake()
        self.assertEqual(vehicle.speed, 13)
        vehicle.brake()
        self.assertEqual(vehicle.speed, 6)

    def test_vehicle_honk(self):
        vehicle = Vehicle("Toyota", "Corolla", 2020)
        self.assertEqual(vehicle.honk(), "HONK!")

    def test_create_car(self):
        car = Car("Toyota", "Corolla", 2020, 4)
        self.assertEqual(car.make, "Toyota")
        self.assertEqual(car.model, "Corolla")
        self.assertEqual(car.year, 2020)
        self.assertEqual(car.speed, 0)
        self.assertEqual(car.num_doors, 4)

    def test_car_honk(self):
        car = Car("Toyota", "Corolla", 2020, 4)
        self.assertEqual(car.honk(), "Beep beep!")

    def test_create_truck(self):
        truck = Truck("Toyota", "Tacoma", 2020, "large")
        self.assertEqual(truck.make, "Toyota")
        self.assertEqual(truck.model, "Tacoma")
        self.assertEqual(truck.year, 2020)
        self.assertEqual(truck.speed, 0)
        self.assertEqual(truck.bed_size, "large")


if __name__ == "__main__":
    unittest.main()
    