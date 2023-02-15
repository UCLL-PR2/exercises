# Vehicle Exercise - difficulty level: **

Create a class called Vehicle that has the following attributes and methods:

- `brand`: a string representing the brand of the vehicle
- `model`: a string representing the model of the vehicle
- `year`: an integer representing the year the vehicle was made
- `speed`: an integer representing the current speed of the vehicle, which starts at 0 value.

The Vehicle class should also have the following methods:

- `accelerate(self, amount)`: increases the speed of the vehicle by `amount`
- `brake(self, amount)`: decreases the speed of the vehicle by `amount`

Then (continue to work in the student.py file), create two subclasses of Vehicle called `Car` and `Truck`.
The `Car` class should have an additional attribute called `num_doors`, and the `Truck` class should have an additional attribute called `bed_size`.

Both the `Car` and `Truck` classes should have their own implementation of the `honk` method that returns a different string.
In the `Car` class this method should return `"Beep beep!"` and in the `Truck` class `"Honk honk!"`.
