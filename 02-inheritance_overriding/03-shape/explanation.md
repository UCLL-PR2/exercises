# Exercise inheritance Shapes
The goal of this exercise is to use inheritance to model different types of shapes, the classes should be coded in the student.py file. In this exercise you will override functions that have the same name but not the same parameters(signature).

To begin, you will need to define a base Shape class that has the following attribute and method:

- **name (a string)**: the name of the shape.
- **\_\_init\_\_() (a method)**: a constructor that takes a name as input. If the name argument is not of type String then raise a **TypeError**. 
- **describe() (a method)**: returns a description of the shape. Example of the description:
```python 
"Circle is a 2D shape"
```
Next, you will need to define several subclasses of Shape that represent specific types of shapes, such as Traingle and Rectangle. Each of these subclasses should have the following attributes and methods:

- **name (a string)**: the name of the shape.
- **sides (list)**: a list of the length of the sides, for example:
```python 
print(traingle.sides) #[3,5,3] the first number represent the left side, the second number represents the bottom side and the right number represent the right side.

print(rectangle.sides) #[3,5] the first number represent the left side and the right side and the second number represents the bottom side and the upper side.
```

- **\_\_init\_\_() (a method)**: a constructor that takes a name and a list of the side lengts as input, and initializes the attributes of the subclass instance using the *super().\_\_init\_\_()* method to set the name attribute inherited from the Shape class. If the sides argument is not of type list then raise a **TypeError**. If the sides argument doesn't exist of a list of 3 numbers then raise a **ValueError**. 
- **describe() (a method)**: a method describe that returns a description of the shape. The subclasses Triangle and Rectangle inherit from Shape and override the describe method.  The describe method in both subclasses are different in the number of parameters they take. The Triangle and the Rectangle class takes in an optional **type** parameter. The type parameter in the Traingle class is default *"scalene"* and for the Rectangle class is *"not a square"*. If the type argument is not of type list then raise a **TypeError**. Example: 

```python 
print(traingle1.describe()) #"Triangle123 is a scalene triangle with [2,3,4] sides"

print(traingle2.describe("isosceles")) #"Triangle456 is a isosceles triangle with [3,4,3] sides"

print(rectangle.describe()) #"Rectangle123 is a not a square rectangle with [4,5] sides"

print(rectangle.describe("square")) #"Rectangle123 is a square rectangle with [4,4] sides"
```
- **\_\_init\_\_() (a method)**: a constructor that takes a name as input and initializes the name attribute of the PetShop instance.
- **add_animal() (a method)**: a method that takes an Animal object as input and adds it to the animals list. If the argument is not of type Animal then raise a **TypeError**.
- **sell_animal() (a method)**: a method that takes an Animal object as input and removes it from the animals list. If the argument is not of type Animal then raise a **TypeError**. If the animal is not in the list then raise a **ValueError**.

To test your solution, you can run the test file and you should create an new file app.py and paste the below code inside it. Try running it and see if you get the same output:
```python 
from app import *


petshop = PetShop("Paws and Claws")

dog1 = Dog("Rover", "Labrador")
dog2 = Dog("Fido", "Poodle")
cat1 = Cat("Fluffy", "Siamese")
parrot1 = Parrot("Polly", "African Grey")
fish1 = Fish("Goldie", "Goldfish")

petshop.add_animal(dog1)
petshop.add_animal(dog2)
petshop.add_animal(cat1)
petshop.add_animal(parrot1)
petshop.add_animal(fish1)

print(petshop.name)
for animal in petshop.animals:
    print(f"{animal.name} ({animal.species}): {animal.make_sound()}")

petshop.sell_animal(dog1)
print("After selling a dog:")
for animal in petshop.animals:
    print(f"{animal.name} ({animal.species}): {animal.make_sound()}")

```
Output:
```text
Paws and Claws
Rover (Dog): Bark
Fido (Dog): Bark
Fluffy (Cat): Meow
Polly (Parrot): Squawk
Goldie (Fish): Bubble bubble
After selling a dog:
Fido (Dog): Bark
Fluffy (Cat): Meow
Polly (Parrot): Squawk
Goldie (Fish): Bubble bubble
```