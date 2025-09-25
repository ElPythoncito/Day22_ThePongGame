from turtle import Turtle

FONT = ("Arial", 60, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update()

    def increase_score_left(self):
        self.l_score += 1
        self.update()

    def increase_score_right(self):
        self.r_score += 1
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.l_score}", font=(FONT), align="center")
        self.goto(100, 200)
        self.write(f"{self.r_score}", font=(FONT), align="center")
