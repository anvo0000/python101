class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")



class Fish(Animal):
    """Fish class is inheritance from Animal"""
    def __init__(self):
        super().__init__() # call Animal init

    def breathe(self):
        super().breathe() #call the Animal breathe function, then modify it.
        print("doing this underwater.")

    def swim(self):
        print("moving in the water")


nemo_fish = Fish()
nemo_fish.breathe()
nemo_fish.swim()