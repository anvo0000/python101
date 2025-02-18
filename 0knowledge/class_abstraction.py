from abc import ABC, abstractmethod # import abstract base class module

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

# Getting error if instantiate an abstract class
# dog = Animal()
# TypeError: Can't instantiate abstract class Animal
# without an implementation for abstract method 'make_sound'

# Dog class inherits from Animal so it has to implement method make_sound
class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"

perfect_dog = Dog()
print(perfect_dog.make_sound())
# Woof! Woof!