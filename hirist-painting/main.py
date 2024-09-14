import turtle as turtle_module
# from turtle import Turtle,Screen
import  random
timmy=turtle_module.Turtle()
screen=turtle_module.Screen()
turtle_module.colormode(255)
timmy.penup()
def random_color():
    r=random.randint(1,255)
    g=random.randint(1,255)
    b=random.randint(1,255)
    return (r,g,b)

timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
rang_number=100
# timmy.position()
for i in range(1,rang_number+1):
    timmy.dot(20,(random_color()))
    timmy.forward(50)
    if i%10==0:

        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)
screen.exitonclick()