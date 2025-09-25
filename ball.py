from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.speed_ball = 0.1

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.teleport(x, y)

    def bounce_y(self):
        self.y_move *= -1
        self.color("white")

    def bounce_x(self):
        self.x_move *= -1
        self.color("white")
        self.speed_ball *= 0.9

    def reset_ball(self):
        self.goto(0, 0)
        self.bounce_x()
