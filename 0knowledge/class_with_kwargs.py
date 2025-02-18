#Create a class with lots of keyword arguments

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")

my_car = Car(make="Honda", color="Red", model="CRV")
your_car = Car(make="Nissan")
print(my_car.color)
print(your_car.color)