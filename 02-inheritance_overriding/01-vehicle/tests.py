import unittest
from student import *

class TestVehicleExercise(unittest.TestCase):
    # TODO Do NOT use the setup method, it makes the tests unreadable and introduces a single point of failure
    # Either
    # * recreate the object in every test method
    # * introduce a factory method that creates whatever objects your test method relies upon
    # * use fixtures
    def setUp(self):
        self.vehicle1 = Vehicle("Toyota", "Corolla", 2020)
        self.car1 = Car("Toyota", "Corolla", 2020, 4)
        self.truck1 = Truck("Toyota", "Tacoma", 2020, "large")
        self.garage = Garage()

    def test_create_vehicle(self):
        vehicle = Vehicle("Toyota", "Corolla", 2020)

        self.assertEqual(vehicle.make, "Toyota")
        self.assertEqual(vehicle.model, "Corolla")
        self.assertEqual(vehicle.year, 2020)
        self.assertEqual(vehicle.speed, 0)

    def test_vehicle_accelerate(self):
        self.assertEqual(self.vehicle1.speed, 0)
        self.vehicle1.accelerate()
        self.assertEqual(self.vehicle1.speed, 10)
        self.vehicle1.accelerate()
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

    def test_add_vehicle(self):
        self.garage.add_vehicle(self.car1)
        self.garage.add_vehicle(self.truck1)

        # Test selling a non-animal object
        with self.assertRaises(TypeError) as context:
            self.garage.add_vehicle(5)
        self.assertEqual(str(context.exception), "The object is not of type 'Vehicle'")

if __name__ == "__main__":
    unittest.main()
