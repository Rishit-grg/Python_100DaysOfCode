import turtle as t
import random
class Food(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("#E7471D")
        self.speed("fastest")
        self.goto(random.randint(-280,280),random.randint(-280,220) )

    def new_posn(self):
        self.goto(random.randint(-280,280),random.randint(-280,220))