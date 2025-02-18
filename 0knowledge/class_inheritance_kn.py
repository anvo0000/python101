class Animal:
    def __init__(self, secret_attribute="Suyt"):
        # __init__: constructor that runs when an object is created.
        # self: refers to the current instance of the class
        self.num_eyes = 2
        self.__secret_attribute = secret_attribute # Private variable

    def breathe(self):
        print("Inhale, exhale.")

    def get_secret_attribute(self):
        return self.__secret_attribute

    def make_sound(self):
        pass  # To be implemented by subclasses



class Fish(Animal):
    """Fish class is inheritance from Animal"""
    def __init__(self):
        super().__init__() # call Animal init

    def breathe(self):
        super().breathe() #call the Animal breathe function, then modify it.
        print("doing this underwater.")

    def swim(self):
        print("moving in the water")


ani = Animal(secret_attribute="Mystery")
print(ani.get_secret_attribute())

nemo_fish = Fish()
nemo_fish.breathe()
nemo_fish.swim()

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.make_sound())  # Calls the correct method based on the object type