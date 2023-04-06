from turtle import Turtle

class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.pencolor("white")
        self.speed("fastest")

    def draw(self):
        self.goto(x=0, y=300)
        self.goto(x=0, y=-300)
