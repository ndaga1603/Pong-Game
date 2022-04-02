

from turtle import Turtle


class Padle1(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.penup()
        self.goto(x=350, y=0)
        self.setheading(90)
        self.showturtle()

    def up(self):
        self.forward(50)

    def down(self):
        self.backward(20)


class Padle2(Padle1):
    def __init__(self):
        super().__init__()
        self.goto(-350, 0)
