import turtle as t

pen = t.Turtle()
paper = t.Screen()


def fwd ():
    pen.forward(10)
def left_10 ():
    pen.left(10)
def right_10 ():
    pen.right(10)
def start_over():
    pen.reset()


paper.listen()

paper.onkey(fwd,"w")
paper.onkey(left_10,"a")
paper.onkey(right_10,"d")
paper.onkey(start_over, "c")
paper.onkey(pen.penup, "Up")
paper.onkey(pen.pendown, "Down")

paper.exitonclick()