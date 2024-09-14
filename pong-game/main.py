
from ball import Ball
from paddle import Paddle
from turtle import Turtle,Screen
from scoreboard import Score
import  time

# screen = Screen_cust()

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.update()
screen.title("pong")
screen.tracer(0)
score=Score()

# ------
r_paddle=Paddle((370,0))
l_paddle=Paddle((-370,0))

# screen.update()


screen.listen()

screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")
screen.onkeypress(l_paddle.go_up,"w")
screen.onkeypress(l_paddle.go_down,"s")

ball=Ball()

game_is_cont=True

while game_is_cont:
    time.sleep(ball.speed_time)
    screen.update()
    ball.move_ball()
    # detect wall collosion
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    #     detect paddle collosion and back ball
    if (ball.distance(r_paddle) < 25 and ball.xcor()>320) or (ball.distance(l_paddle) < 25 and ball.xcor() <-320):
        ball.x_bounce()
    # Detect right paddle misses
    if  ball.xcor() >390 :
        ball.reset_ball()
        ball.x_bounce()

        score.l_score_point()


    if  ball.xcor()<-380:
        ball.reset_ball()
        ball.x_bounce()
        score.r_score_point()




screen.exitonclick()
