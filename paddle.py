from turtle import Turtle
import random


class Paddle(Turtle):
    def __init__(self, x, y, color_list):
        super().__init__()
        self.color_paddle = color_list
        self.shape("square")
        self.color(random.choice(color_list))
        self.penup()
        self.left(90)
        self.shapesize(1, 5)
        self.teleport(x, y)

    def up(self):
        self.forward(10)

    def down(self):
        self.backward(10)

    def change_color(self):
        self.color(random.choice(self.color_paddle))
