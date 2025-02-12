from turtle import Turtle

SCOREBOARD_X = 0
SCOREBOARD_Y = 250
ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')
DATA = "data.txt"

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.load_last_high_score() or 0

        self.color("white")
        self.penup()
        self.goto(SCOREBOARD_X, SCOREBOARD_Y)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}",
                   align=ALIGNMENT,
                   font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg=f"GAME OVER",
    #                align=ALIGNMENT,
    #                font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
        self.update_scoreboard()

    def load_last_high_score(self):
        with open(DATA) as data:
            content = int(data.read())
            self.high_score = content
            print(f"Load HighScore from file data.txt: {self.high_score}")
        return  self.high_score

    def save_high_score(self):
        with open(DATA, "w") as data:
            data.write(str(self.high_score))
            print(f"Save HighScore to data.txt: {self.high_score}")