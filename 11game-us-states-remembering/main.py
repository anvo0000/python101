# import turtle
from turtle import Turtle, Screen

import pandas as pd
df = pd.read_csv(filepath_or_buffer="50_states.csv")

FONT = ("Courier", 24, "normal")
def game_over(self):
    self.goto(0,0)
    self.write(f"CONGRATULATION! You did it!",
               align="center",
               font=FONT)

image = "blank_states_img.gif"
screen = Screen()
turtle = Turtle()
screen.title("U.S State Game")
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

state_turtle = Turtle()
state_turtle.hideturtle()
state_turtle.penup()

correct_score = 0
game_is_on = True
user_states = []
all_states = df["state"].to_list() # get the list of state

while game_is_on:
    user_answer = screen.textinput(title=f"{correct_score}/50 States Correct",
                                   prompt="What's another state name?",
                                   )
    user_answer = user_answer.title()
    print(f"user_guess: {user_answer}")

    if user_answer in all_states:
        user_states.append(user_answer)
        row = df[df["state"] == user_answer]
        x = row["x"].item()
        y = row["y"].item()

        print(f"data-position: {x, y}")
        state_turtle.goto(x, y)
        state_turtle.write(user_answer)
        correct_score += 1
        screen.update()

    if correct_score == 50:
        game_over()
        game_is_on = False

    if user_answer == "Exit":
        game_is_on = False
        # write the remaining states to states_to_learn.csv

        # # Option 1: [Using Set()] in
        # states_to_learn = list(set(all_states) - set(user_states))

        # Option 2: Using List Comprehension
        states_to_learn = [state for state in all_states if state not in user_states]

        df = pd.DataFrame(data=states_to_learn, columns=["states to learn"])
        df.to_csv("states_to_learn.csv")
screen.mainloop()


