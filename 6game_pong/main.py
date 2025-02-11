from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

BG_COLOR = "black"
GAME_NAME = "Pong Game"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


#Set up Screen
# turn off the tracer, nothing will happen,
# until we call screen.update() the screen will change
screen = Screen()
screen.tracer(0)
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(BG_COLOR)
screen.title(GAME_NAME)

#create r_paddle and l_paddle and on_screen listen keys
r_paddle = Paddle(direction="right")
l_paddle = Paddle(direction="left")

screen.listen()
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")

#create a ball
ball = Ball()

#scoreboard
scoreboard = ScoreBoard()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update() #screen update and ready to receive keyboard movement requests.
    ball.move()

    #Detect the collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280: #-20 for each ycor() to reserve the ball's wid
        ball.bounce_y()  # the ball bounce back

    #Detect collision with r_paddle and l_paddle
    if (
            (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or
            (ball.distance(l_paddle) < 50 and ball.xcor() < -320)
    ):
        ball.bounce_x()

    # Detect when r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect when l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()