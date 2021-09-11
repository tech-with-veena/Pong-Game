from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time
screen=Screen()
screen.bgcolor("black")
screen.setup(height=600,width=800)
screen.title("Pong")
screen.tracer(0)
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Score()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")


gameison=True
while gameison:
    time.sleep(ball.movespeed)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bouncey()
    if ball.distance(r_paddle) < 50 and ball.xcor() < 320 or ball.distance(l_paddle) < 50 and ball.ycor() < -320:
        ball.bouncex()
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.lpoint()
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.rpoint()

screen.exitonclick()
