from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("slowest")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.ball_speed = 1
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def bounce(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1

    def ball_reset(self):
        self.hideturtle()
        self.speed("fastest")
        self.showturtle()
        self.goto(x=0, y=0)
        self.speed("slowest")
        self.bounce_paddle()

    def speed_up(self):
        self.speed(self.ball_speed + 1)




