import turtle
from turtle import Turtle, Screen
from random import choice, randint

da_vinci = Turtle()
da_vinci.pensize(1)
screen = Screen()
da_vinci.speed(100)
screen.colormode(255)

turn = 1
for _ in range(int(360/turn)):
    da_vinci.forward(2)
    da_vinci.right(turn)
    da_vinci.pencolor(randint(1,255),randint(1,255),randint(1,255))
    da_vinci.circle(100)

screen.exitonclick()
