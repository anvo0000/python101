from turtle import Turtle

SCOREBOARD_X = 0
SCOREBOARD_Y = 250
ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(SCOREBOARD_X, SCOREBOARD_Y)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}",
                   align=ALIGNMENT,
                   font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER",
                   align=ALIGNMENT,
                   font=FONT)

