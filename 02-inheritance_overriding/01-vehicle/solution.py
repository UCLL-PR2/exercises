class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self):
        self.speed += 10

    def brake(self):
        self.speed -= 7

    def honk(self):
        return "HONK!"

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def honk(self):
        return "Beep beep!"

class Truck(Vehicle):
    def __init__(self, make, model, year, bed_size):
        super().__init__(make, model, year)
        self.bed_size = bed_size

    def honk(self):
        return "Honk honk!"

class Garage:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)