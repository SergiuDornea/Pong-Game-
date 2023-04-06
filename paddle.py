from turtle import Turtle
MOVE_DISTANCE = 20



class Paddle(Turtle):

    def __init__(self, positions):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5.0, stretch_len=1.0)
        self.penup()
        self.speed("fastest")
        self.goto(positions[0], positions[1])
        self.showturtle()

    def up(self):
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y)

