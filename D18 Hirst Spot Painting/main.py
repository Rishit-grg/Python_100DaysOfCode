import colorgram
from turtle import Turtle, Screen
import random

# Import Hists colour Palette using colorgram

colours = colorgram.extract("Hirst_sample.jpg", 30)
palette = []

for i in range(len(colours)):
    r = colours[i].rgb.r
    g = colours[i].rgb.g
    b = colours[i].rgb.b
    palette.append((r,g,b))

print(len(palette))
# Removing background colors from palette
for color in palette:
    filter_light = 180
    if color[0] > filter_light and color[1] > filter_light and color[2] > filter_light:
        palette.remove(color)

print(len(palette))


# making the artwork
hirst = Turtle()
hirst.penup()
hirst.hideturtle()
screen = Screen()
screen.colormode(255)
step = 25
for _ in range(10):
    for _ in range(10):
        hirst.forward(step)
        hirst.dot(15, random.choice(palette))
    hirst.speed(10)
    hirst.left(90)
    hirst.forward(step)
    hirst.left(90)
    hirst.forward(step*10)
    hirst.left(180)
    hirst.speed(1)

screen.exitonclick()