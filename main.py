from turtle import Screen, Turtle
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
x_position = [0,-20, -40 ]
segments = []

for turtle_index in range(0,3):
    segment = Turtle(shape="square")
    # new_turtle.shape("square")
    segment.color("white")
    segment.penup()
    segment.pensize(20)
    segment.setposition(x=x_position[turtle_index],y = 0)
    segments.append(segment)

screen.update()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments) -1 ,0,-1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)

















screen.exitonclick()