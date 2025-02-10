"""
Documentation: https://docs.python.org/3/library/turtle.html
Color https://cs111.wellesley.edu/reference/colors
"""
from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

# draw a rectangle
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)

for i in range(20):
    if i % 2 == 0:
        timmy_the_turtle.forward(10)
        timmy_the_turtle.pendown()
    else:
        timmy_the_turtle.forward(10)
        timmy_the_turtle.penup()


# for _ in range(4):
#     timmy_the_turtle.forward(400)
#     timmy_the_turtle.right(90)

screen = Screen()
screen.exitonclick()