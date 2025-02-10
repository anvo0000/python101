from turtle import Turtle, Screen

import random
tim = Turtle()
screen = Screen()
screen.colormode(1)
screen.colormode(255)
tim.speed(speed="fastest")
tim.shapesize(outline=8)
tim.pensize(5)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_shape(num_sides):
    angle = 360 /num_sides

    tim.color(random_color())
    for _ in range(num_sides):
        tim.forward(distance=100)
        tim.right(angle)

for shape_side_n in range(3,11):
    draw_shape(shape_side_n)

screen.exitonclick()