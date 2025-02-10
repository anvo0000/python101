from turtle import Turtle, Screen
import random
import tkinter.messagebox

#Screen setup
screen = Screen()
screen.setup(width=500, height=400)

def clear_drawing(turtle):
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


def game():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    user_bet = screen.textinput(title="Make your bet",
                                prompt=f"Which turtle will win the race?\nEnter a color ({", ".join(colors)}): ")
    is_race_on = False
    all_turtles = []

    y_position = [-70, -40, -10, 20, 50, 80]
    for turtle_index in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.goto(x=-230, y=y_position[turtle_index])
        all_turtles.append(new_turtle)

    if user_bet:
        is_race_on = True

    while is_race_on:
        for turtle in all_turtles:
            turtle.speed("fastest")

            random_distance = random.randint(0, 20)
            # random_distance = 15 if turtle.pencolor() == "blue" else random_distance
            turtle.forward(random_distance)

            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"{winning_color} is win!")
                    screen.textinput(title="Game Over",
                                     prompt=f"You win! The {winning_color} is the winner.")
                    print(f"The {winning_color} turtle is the winner!")
                else:
                    screen.textinput(title="Game Over",
                                     prompt=f"You've lost! The {winning_color} is the winner")
                    print(f"You've lost! The {winning_color} turtle is the winner!")

        if is_race_on == False:
            break

def main():
    turn = 0
    while True:
        if turn==0:
            game()
        start_new_game = screen.textinput(title="Continue?",
                         prompt=f"Press Enter to Continue. 'exit' to end game")
        if start_new_game != "exit":
            game()
        else:
            screen.onkey(key="exit", fun=screen.bye)
            break

game()
# main()
screen.exitonclick()

