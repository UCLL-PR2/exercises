# Exercise inheritance Animals
The goal of this exercise is to get familiar with multiple inheritance:

Consider a scenario where you're creating a class hierarchy for a Zoo. You have base classes **Animal** and **Enclosure**

The **Animal class** has the following attributes:

- **name**: a string representing the name of the animal
- **species**: a string representing the species of the animal
- **age**: an integer representing the age of the animal

The **Animal class** has the following methods:

- **make_sound**: returns a string representing the sound the animal makes

The **Enclosure class** has the following attributes:

- **name**: a string representing the name of the enclosure
- **capacity**: an integer representing the maximum number of animals that can be housed in the enclosure
The Enclosure class has the following methods:

- **add_animal**: accepts an Animal object and adds it to the enclosure (as long as the enclosure isn't already full)
- **remove_animal**: removes an Animal object from the enclosure (as long as it's in the enclosure)

Your task is to create a class **ZooAnimal** that inherits from both **Animal** and **Enclosure**. The ZooAnimal class should have all the attributes and methods of both base classes.

In the student.py some starting code is already given. You should implement the **ZooAnimal class**.

After implementation the you can test your code by executing the next code:
```python 
a = Animal("Giraffe", "Giraffa camelopardalis", 5)
e = Enclosure("African Savanna", 10)
z = ZooAnimal("Giraffe", "Giraffa camelopardalis", 5, "African Savanna", 10)

print(a.name) # Output: "Giraffe"
print(e.capacity) # Output: 10

print(z.name) # Output: "Giraffe"
print(z.capacity) # Output: 10

e.add_animal(a)
print(len(e.animals)) # Output: 1

e.remove_animal(a)
print(len(e.animals)) # Output: 0

