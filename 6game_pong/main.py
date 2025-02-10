from turtle import Screen,Turtle
from paddle import Paddle

BG_COLOR = "black"
GAME_NAME = "Pong Game"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

PADDLE_SHAPE = "square"
PADDLE_COLOR = "white"
PADDLE_X = 350
PADDLE_Y = 0
STRETCH_WID = 5
STRETCH_LEN = 1
PADDLE_MOVE = 20

#Set up Screen
# turn off the tracer, nothing will happen,
# until we call screen.update() the screen will change
screen = Screen()
screen.tracer(0)
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(BG_COLOR)
screen.title(GAME_NAME)

#create r_paddle
r_paddle = Paddle(direction="right")
l_paddle = Paddle(direction="left")

screen.listen()
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")

screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")


game_is_on = True
while game_is_on:
    screen.update() #screen update and ready to receive keyboard movement requests.

screen.mainloop()