class Dog:
    # use of default functions.
    def __init__(self, name, age="No age was selected"):
        self.name = name
        self.age = age
        
    def bark(self):
        print(f"Dog name {self.name}, Age : {self.age} !")

# create a dog object

rex = Dog("Rex")
rex.bark()

class Animal:
    def __init__(self, species):
        self.species = species

class Terrestrial(Animal):
    def __init__(self):
        super().__init__("Terrestrial")

    def walk(self):
        print("This animal walks on land.")

class Aquatic(Animal):
    def __init__(self):
        super().__init__("Aquatic")

    def swim(self):
        print("This animal swims in water.")

class Amphibian(Terrestrial, Aquatic):
    pass

frog = Amphibian()
frog.walk()
frog.swim()
