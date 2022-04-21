from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.total_score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.total_score}          High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.total_score > self.high_score:
            self.high_score = self.total_score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.total_score = 0
        self.update_scoreboard()

    def add_point(self):
        self.clear()
        self.total_score += 1
        self.update_scoreboard()
