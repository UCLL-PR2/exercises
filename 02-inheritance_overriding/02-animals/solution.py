class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return "Some generic animal sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def make_sound(self):
        return "Bark"

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Cat")
        self.breed = breed

    def make_sound(self):
        return "Meow"

class Parrot(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Parrot")
        self.breed = breed

    def make_sound(self):
        return "Squawk"

class Fish(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Fish")
        self.breed = breed

    def make_sound(self):
        return "Bubble bubble"

class PetShop:
    def __init__(self, name):
        self.name = name
        self.animals = []
    
    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
        else:
            raise TypeError("The object is not of type 'Animal'")
    
    def sell_animal(self, animal):
        if isinstance(animal, Animal):
            if animal in self.animals:
                self.animals.remove(animal)
            else:
                raise ValueError("This animal is not available!")
        else:
            raise TypeError("The object is not of type 'Animal'")
    



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