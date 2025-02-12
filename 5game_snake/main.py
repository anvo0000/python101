from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

BG_COLOR = "black"
GAME_NAME = "Snake Game"

SNAKE_SHAPE = "square"
SNAKE_COLOR = "red"
FOOD_SHAPE = "turtle"
FOOD_COLOR = "green"

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor(BG_COLOR)
screen.title(GAME_NAME)
screen.tracer(0)  # turn off the tracer, nothing will happen, until we call screen.update() the screen will change

snake = Snake(snake_shape=SNAKE_SHAPE,snake_color=SNAKE_COLOR)
food = Food(food_shape=FOOD_SHAPE, food_color=FOOD_COLOR)
scoreboard = ScoreBoard()

game_is_on = True
screen.listen()

count = 0
while game_is_on:
    time.sleep(0.3)
    screen.update()  # wait 0.1 second and then update the screen
    count += 1
    snake.move()

    screen.onkey(key="Up", fun=snake.up)  # no () right after move_forward function
    screen.onkey(key="Down", fun=snake.down)
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="Right", fun=snake.right)

    # Detect the collision of the Snake Head with Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        scoreboard.update_scoreboard()

    # Detect the head's collision with its tail
    #ignore the snake's head by slicing snake.segments[1:]
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # scoreboard.game_over()
            # game_is_on = False
            scoreboard.reset()
            snake.reset()

    # Detect collision with the wall
    # if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    # abs(snake.head.xcor()) > 280 checks if xcor is greater than 280 or less than -280 in one step.
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        # scoreboard.game_over()
        # game_is_on = False
        scoreboard.reset()
        snake.reset()

    if count == 500:
        break

screen.mainloop()
