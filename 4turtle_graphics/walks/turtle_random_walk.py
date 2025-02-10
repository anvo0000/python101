from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.speed(speed="fastest")
tim.shape("turtle")
tim.speed(speed="fastest")
tim.shapesize(outline=8)
tim.pensize(15)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def random_walk():
    directions = [0, 90, 180, 270]
    for _ in range(100):
        tim.color(random_color())
        tim.forward(distance=30)
        tim.setheading(random.choice(directions))


random_walk()
screen.exitonclick()