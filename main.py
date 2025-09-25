# -------------------------------------------------------- EL PYTHONCITO XD 🐍🐍🐍🐍
from turtle import Screen
from paddle import Paddle
from ball import Ball
from colors import colors1, colors2
from scoreboard import Score
import time

my_screen = Screen()

# ------------------------------------------------------------------ My Screen
my_screen.setup(width=800, height=600)
my_screen.bgcolor("black")
my_screen.title("The Pong Game 🐍")
my_screen.tracer(0)

# ------------------------------------------------------------------------------ My objects
right_paddle = Paddle(x=350, y=0, color_list=colors1)
left_paddle = Paddle(x=-350, y=0, color_list=colors2)
ball = Ball()
score = Score()

my_screen.listen()
my_screen.onkeypress(key="Up", fun=right_paddle.up)
my_screen.onkeypress(key="Down", fun=right_paddle.down)
my_screen.onkeypress(key="w", fun=left_paddle.up)
my_screen.onkeypress(key="s", fun=left_paddle.down)

game_over = False
while not game_over:
    my_screen.update()
    time.sleep(ball.speed_ball)
    ball.move()

    # Bounce y
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Bounce x
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        right_paddle.change_color()
    elif ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        left_paddle.change_color()

    if ball.xcor() > 350:
        ball.reset_ball()
        score.update()
        score.increase_score_left()

    if ball.xcor() < -350:
        ball.reset_ball()
        score.update()
        score.increase_score_right()

 # ------------------------------------------------- Exit
my_screen.exitonclick()
