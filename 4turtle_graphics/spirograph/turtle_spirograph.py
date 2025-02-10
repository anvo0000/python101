from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.speed(speed="fastest")
tim.shape("turtle")
tim.speed(speed="fastest")
# new_turtle.shapesize(outline=8)
# new_turtle.pensize(15)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(radius=100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(1)


screen.exitonclick()