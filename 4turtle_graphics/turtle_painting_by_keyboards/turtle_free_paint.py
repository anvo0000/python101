from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.shape("turtle")

def move_forward():
    tim.forward(distance=10)

def move_backward():
    tim.backward(distance=10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="Up", fun=move_forward) # no () right after move_forward function
screen.onkey(key="Down", fun=move_backward)
screen.onkey(key="Left", fun=turn_left)
screen.onkey(key="Right", fun=turn_right)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()
