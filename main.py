from turtle import Screen
from paddle import Paddle
from ball import Ball
from line import Line
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")



positions_right_paddle = [350, 0]
positions_left_paddle = (-350, 0)
paddle_right = Paddle(positions_right_paddle)
paddle_left = Paddle(positions_left_paddle)
ball = Ball()
line = Line()
line.draw()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")
screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s")


game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    # bounce on wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    # bounce on paddle
    if ball.xcor() > 320 and ball.distance(paddle_right) < 50 or ball.xcor() < -320 and ball.distance(paddle_left) < 50:
        ball.bounce_paddle()
        ball.speed_up()

    # ball hits the side walls and game restarts
    # r side
    if ball.xcor() > 380:
        ball.ball_reset()
        scoreboard.l_point()
    # l side
    if ball.xcor() < -380:
        ball.ball_reset()
        scoreboard.r_point()




screen.exitonclick()
