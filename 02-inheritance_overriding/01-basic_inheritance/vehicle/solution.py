class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def description(self):
        return self.make + " " + self.model + " (" + str(self.year) + ")"

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        Car.__init__(self, make, model, year)
        self.battery_size = battery_size
        
    def range(self):
        if self.battery_size == 60:
            return 140
        elif self.battery_size == 85:
            return 240
        else:
            return "Range not available for this battery size."

