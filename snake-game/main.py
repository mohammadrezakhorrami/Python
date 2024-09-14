from turtle import Turtle,Screen
from snak import Snake
from food import Food
from scoreboard import Score
import  time


screen=Screen()
timmy=Turtle()


screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake=Snake()
food=Food()
score=Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")




# for position in position_turtle:
#      new_turt=Turtle("square")
#      new_turt.color("white")
#      new_turt.penup()
#      new_turt.goto(position)
#      turtule_list.append(new_turt)

        # turtule_list(position).forward(20)
screen.update()
is_continue=True
#
while is_continue:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<20:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() <-290:
        # is_continue=False
        # score.game_over()
        score.reset()
        snake.reset()
    # define collesion
    for segment in snake.turtule_list[1:]:
        # if segment==snake.head:
        #     pass
        if snake.head.distance(segment)<10:
            # is_continue=False
            # score.game_over()
            score.reset()
            snake.reset()


# # for i in range(10):
#     for seg in range(len(turtule_list)-1,0,-1):
#         x=turtule_list[seg-1].xcor()
#         y = turtule_list[seg - 1].ycor()
#         turtule_list[seg].goto(x,y)
#         # turtule_list[seg].left(90)
#     turtule_list[0].forward(20)
#     # turtule_list[0].right(90)















screen.exitonclick()