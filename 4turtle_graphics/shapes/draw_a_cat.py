import turtle

# Setup turtle
t = turtle.Turtle()
t.speed("fastest")
t.pensize(3)
screen = turtle.Screen()
screen.bgcolor("white")

# Function to draw a circle
def draw_circle(x, y, radius, color):
    t.penup()
    t.goto(x, y - radius)  # Move to the correct start position
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Draw face
draw_circle(0, 0, 100, "gray")

# Draw left ear
t.penup()
t.goto(-80, 90)
t.pendown()
t.fillcolor("gray")
t.begin_fill()
t.goto(-120, 160)
t.goto(-40, 140)
t.goto(-80, 90)
t.end_fill()

# Draw right ear
t.penup()
t.goto(80, 90)
t.pendown()
t.begin_fill()
t.goto(120, 160)
t.goto(40, 140)
t.goto(80, 90)
t.end_fill()

# Draw eyes
draw_circle(-40, 30, 15, "white")  # Left eye
draw_circle(40, 30, 15, "white")   # Right eye
draw_circle(-40, 30, 7, "black")   # Left pupil
draw_circle(40, 30, 7, "black")    # Right pupil

# Draw nose
draw_circle(0, 0, 10, "pink")

# Draw whiskers
t.penup()
t.goto(-50, -10)
t.pendown()
t.goto(-100, -20)

t.penup()
t.goto(-50, 0)
t.pendown()
t.goto(-100, 0)

t.penup()
t.goto(-50, 10)
t.pendown()
t.goto(-100, 20)

t.penup()
t.goto(50, -10)
t.pendown()
t.goto(100, -20)

t.penup()
t.goto(50, 0)
t.pendown()
t.goto(100, 0)

t.penup()
t.goto(50, 10)
t.pendown()
t.goto(100, 20)

# Hide turtle and finish
t.penup()
t.hideturtle()
turtle.done()
