class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self, amount):
        self.speed += amount

    def brake(self, amount):
        self.speed -= amount


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

    def honk(self) -> str:
        return "Honk honk!"
