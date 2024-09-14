from turtle import Turtle
position_turtle=[(0,0),(-20,0),(-40,0)]
move_snake_distance=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.turtule_list=[]
        self.create_snake()
        self.head=self.turtule_list[0]
        self.score=0

    def create_snake(self):
        position_turtle = [(0, 0), (-20, 0), (-40, 0)]
        turtule_list = []

        for position in position_turtle:
            self.add_segment(position)

    def add_segment(self,position):
        new_turt = Turtle("square")
        new_turt.color("white")
        new_turt.penup()
        new_turt.goto(position)
        self.turtule_list.append(new_turt)

    def reset(self):
        for trl in  self.turtule_list:
            trl.goto(10000,10000)
        self.turtule_list.clear()
        self.create_snake()
        self.head = self.turtule_list[0]

    def extend(self):

         self.add_segment(self.turtule_list[-1].position())

    def move(self):
           for seg in range(len(self.turtule_list) - 1, 0, -1):
                x = self.turtule_list[seg - 1].xcor()
                y = self.turtule_list[seg - 1].ycor()
                self.turtule_list[seg].goto(x, y)
                # turtule_list[seg].left(90)
           self.head.forward(move_snake_distance)

    def up(self):
        if  self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def  down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != LEFT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(RIGHT)

