from turtle import Turtle


STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
SNAKE_SPEED = "fastest"

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():
    def __init__(self, snake_shape="square", snake_color="white"):
        self.segments = []
        self.snake_shape = snake_shape
        self.color = snake_color
        self.create_snake()
        self.head = self.segments[0]  # the first segment is the snake's head

    def create_snake(self):
        for pos in STARTING_POSITION:
            self.add_segment(position=pos)

    def add_segment(self, position):
        """add a new segment to the snake"""
        new_segment = Turtle(self.snake_shape)
        new_segment.color(self.color)
        new_segment.penup()
        new_segment.goto(position)
        new_segment.speed(SNAKE_SPEED)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)

        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        """Snake go to North
        Accept to go Up, if it is on LEFT OR RIGHT
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Snake go to South"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        """Snake go Right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        """Snake go Left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
