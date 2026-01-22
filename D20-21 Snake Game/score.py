import turtle

class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = -1

    def update_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score: {self.score}", move=False, align='center', font=('Arial', 15, 'normal'))
