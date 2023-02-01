class Vehicle:
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self):
        self.speed += 10

    def brake(self):
        self.speed -= 7

    def honk(self) -> str:
        return "HONK!"

class Car(Vehicle):
    def __init__(self, make: str, model: str, year: int, num_doors: int):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def honk(self) -> str:
        return "Beep beep!"

class Truck(Vehicle):
    def __init__(self, make: str, model: str, year: int, bed_size: str):
        super().__init__(make, model, year)
        self.bed_size = bed_size

    def honk(self) -> str:
        return "Honk honk!"

class Garage:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle: Vehicle):
        if isinstance(vehicle, Vehicle):
            self.vehicles.append(vehicle)
        else:
            raise TypeError("The object is not of type 'Vehicle'")