from turtle import Turtle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

PADDLE_SHAPE = "square"
PADDLE_COLOR = "white"
PADDLE_LEFT_X = -350
PADDLE_RIGHT_X = 350
PADDLE_Y = 0
STRETCH_WID = 5
STRETCH_LEN = 1
PADDLE_MOVE = 40

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
        new_y = self.paddle.ycor() + PADDLE_MOVE
        if new_y > SCREEN_HEIGHT/2:
            new_y = SCREEN_HEIGHT/2

        print(f"Moving up new_y: {new_y}")
        self.paddle.goto(self.paddle.xcor(), new_y)

    def go_down(self):
        new_y = self.paddle.ycor() - PADDLE_MOVE
        if new_y < (SCREEN_HEIGHT/2 * -1):
            new_y = SCREEN_HEIGHT/2 * -1

        self.paddle.goto(self.paddle.xcor(), new_y)
        print(f"Moving down new_y: {new_y}")



