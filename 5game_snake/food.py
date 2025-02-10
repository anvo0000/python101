import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self, food_shape="circle", food_color="red"):
        """Food is inherited from Turtle, so we can use snake_shape, penup, shapesize directly in Food"""
        super().__init__()
        self.shape(food_shape)
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.color(food_color)
        self.refresh()

    def refresh(self):
        """The screen is 600 x 600, so we have X= -300 - 0 - 300, Y= -300 - 0 - 300
        We don't want the food is on the corner, so random pos have to eliminate -300 and 300"""
        random_x = random.randint(-200, 200)
        random_y = random.randint(-200, 200)
        self.goto(random_x, random_y)
