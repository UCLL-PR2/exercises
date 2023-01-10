# Vehicle Exercise
Create a class called Vehicle that has the following attributes and methods:

- **brand**: a string representing the brand of the vehicle
- **model**: a string representing the model of the vehicle
- **year**: an integer representing the year the vehicle was made
- **speed**: an integer representing the current speed of the vehicle, which starts at 0 value.

The Vehicle class should also have the following methods:

- **accelerate**: increases the speed of the vehicle by 10
- **brake**: decreases the speed of the vehicle by 7
- **honk**: returns the string "HONK!"

Then (continue to work in the student.py file), create two subclasses of Vehicle called Car and Truck. The Car class should have an additional attribute called **num_doors**, and the Truck class should have an additional attribute called **bed_size**. 

Both the Car and Truck classes should have their own implementation of the **honk method** that returns a different string. In the Car class this method should return *"Beep beep!"* and in the Truck class *"Honk honk!"*.

Next, create a class called Garage that has a single attribute, vehicles, which is a list of Vehicle objects. The Garage class should have a method called **add_vehicle** which takes a Vehicle object as an argument and adds it to the vehicles list.