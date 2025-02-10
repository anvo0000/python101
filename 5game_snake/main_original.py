from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) # turn off the tracer, nothing will happen, until we call screen.update() the screen will change

segments = []
starting_position = [(0,0),(-20,0), (-40,0)]
for pos in starting_position:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(pos)
    segments.append(new_segment)

game_is_on = True

count = 0
while game_is_on:
    time.sleep(0.1); screen.update(); #wait 0.1 second and then update the screen
    count+= 1

    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)

    segments[0].forward(20)
    segments[0].left(90)

    if count ==20:
        break

screen.exitonclick()