# Exercise inheritance Animals
The goal of this exercise is to use inheritance to model different types of animals and a pet shop that sells them, the classes should be coded in the student.py file.
To begin, you will need to define a base Animal class that has the following attributes and methods:

- **name (a string)**: the name of the animal.
- **species (a string)**: the species of the animal.
- **make_sound() (a method)**: returns a string representing the sound that the animal makes.

Next, you will need to define several subclasses of Animal that represent specific types of animals, such as dogs, cats, parrots, and fish. Each of these subclasses should have the following attributes and methods:

- **breed (a string)**: the breed of the animal.
- **\_\_init\_\_() (a method)**: a constructor that takes a name and a breed as input, and initializes the attributes of the subclass instance using the *super().\_\_init\_\_()* method to set the name and species attributes inherited from the Animal class.
- **make_sound() (a method)**: a method that returns a string representing the sound that the animal makes. This method should override the make_sound() method inherited from the Animal class.
Finally, you will need to define a PetShop class that has the following attributes and methods:
- **name (a string)**: the name of the pet shop.
- **animals (a list)**: a list of Animal objects that are currently for sale in the pet shop.
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