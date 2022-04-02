
from turtle import Screen, Turtle, speed
from padle import Padle1, Padle2
from ball import Ball
from score import Score
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

pad_1 = Padle1()
pad_2 = Padle2()
ball = Ball()
score = Score()

screen.listen()
screen.onkey(fun=pad_1.up, key="Up")
screen.onkey(fun=pad_1.down, key="Down")
screen.onkey(fun=pad_2.up, key="w")
screen.onkey(fun=pad_2.down, key="s")


is_game_on = True
while is_game_on:
    time.sleep(ball.speed_times)
    screen.update()
    ball.move()

    # detect collision with a wall
    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.bounce_back_y()

    # detect collision with the padles
    if (ball.distance(pad_1) < 50 and ball.xcor() > 320) or (ball.distance(pad_2) < 50 and ball.xcor() < -320):
        ball.bounce_back_x()

    if ball.xcor() > 380:
        ball.reset_ball()
        score.increase_left_score()

    if ball.xcor() < -380:
        ball.reset_ball()
        score.increase_right_score()


screen.exitonclick()
