from turtle import Turtle
x_cor=10
y_cor=10
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.xps=x_cor
        self.yps=y_cor
        self.speed_time=0.1

    def move_ball(self):
        x_pos=self.xcor() +self.xps
        y_pos=self.ycor() +self.yps
        self.goto(x_pos,y_pos)

    def bounce(self):
        self.yps *=-1
    def x_bounce(self):
        self.xps *=-1
        self.speed_time *=0.9


    def reset_ball(self):
        self.speed_time=0.1
        self.goto(0, 0)



