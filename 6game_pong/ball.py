from turtle import Turtle

BALL_WIDTH = 20
BALL_HEIGHT = 20
BALL_X = 0
BALL_Y = 0
BALL_SHAPE = "circle"
BALL_COLOR = "white"
RESET_MOVE_SPEED = 0.1

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(BALL_SHAPE)
        self.color(BALL_COLOR)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = RESET_MOVE_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        # print(f"new pos: {new_x}, {new_y}")
        self.goto(x=new_x, y=new_y)

    def bounce_y(self):
        self.y_move *= -1
        # print(f"Change direction: ball.y_move {self.y_move}")

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
        # print(f"Change direction: ball.y_move {self.x_move}")

    def reset_position(self):
        self.goto(x=0, y=0)
        self.move_speed = RESET_MOVE_SPEED
        self.bounce_x()