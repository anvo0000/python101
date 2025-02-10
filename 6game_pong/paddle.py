from turtle import Turtle

PADDLE_SHAPE = "square"
PADDLE_COLOR = "red"
PADDLE_LEFT_X = -350
PADDLE_RIGHT_X = 350
PADDLE_Y = 0
STRETCH_WID = 5
STRETCH_LEN = 1
PADDLE_MOVE = 20

class Paddle(Turtle):
    def __init__(self, direction="right"):
        super().__init__() # constructor of Turtle
        self.paddle = Turtle(shape=PADDLE_SHAPE)
        self.direction = direction # direction: accepts 'left' or 'right' only
        self.create_paddle()
        print(self.direction)

    def create_paddle(self):
        self.paddle.color(PADDLE_COLOR)
        self.paddle.penup()
        direction_x = PADDLE_LEFT_X if self.direction=="left" else PADDLE_RIGHT_X
        self.paddle.goto(x=direction_x, y=PADDLE_Y)
        self.paddle.shapesize(stretch_wid=STRETCH_WID, stretch_len=STRETCH_LEN)

    def go_up(self):
        print("Moving up")
        new_y = self.paddle.ycor() + PADDLE_MOVE
        self.paddle.goto(self.paddle.xcor(), new_y)

    def go_down(self):
        print("Moving down")
        new_y = self.paddle.ycor() - PADDLE_MOVE
        self.paddle.goto(self.paddle.xcor(), new_y)


# r_paddle = Paddle()
# while True:
#     r_paddle.go_up()
#
