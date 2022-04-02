
from turtle import Turtle


class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.goto(-180, 200)
        self.write(f"{self.left_score}", font=("courier", 80, "normal"))
        self.goto(180, 200)
        self.write(f"{self.right_score}", font=("courier", 80, "normal"))

    def increase_left_score(self):
        self.left_score = self.left_score + 1
        self.clear()
        self.update_score()

    def increase_right_score(self):
        self.right_score = self.right_score + 1
        self.clear()
        self.update_score()
