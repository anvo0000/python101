# pip install colorgram.py
from turtle import Turtle, Screen
import random

import colorgram


def extract_color_list():
    rgb_colors= []
    colors = colorgram.extract('Hirst_original_painting.jpg', 30)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)
    return rgb_colors

# color_list = extract_color_list()
# print(color_list)
color_list = [(241, 236, 230), (210, 151, 100), (68, 100, 130), (147, 86, 62), (128, 161, 184), (210, 223, 230), (239, 224, 229), (138, 72, 95), (229, 238, 233), (195, 133, 156), (205, 95, 70), (148, 147, 70), (68, 117, 86), (122, 174, 148), (225, 200, 124), (185, 94, 121), (35, 50, 70), (45, 56, 104), (52, 43, 32), (94, 153, 112), (103, 120, 166), (52, 39, 53), (75, 150, 166), (230, 167, 187), (235, 172, 161), (104, 45, 37), (34, 54, 42), (102, 44, 66), (161, 209, 189), (154, 208, 219)]

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.speed("fastest")

tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    tim.dot(20,random.choice(color_list) )
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

tim.hideturtle()
screen.exitonclick()