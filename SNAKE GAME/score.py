import turtle

TEXT_SIZE = 15

class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0

    def show_score(self):
        self.write(f"Score: {self.score}", move=False, align='center', font=('Courier', TEXT_SIZE, 'normal'))

    def update_score(self):
        self.score+=1
        self.clear()
        self.show_score()

    def game_over(self):
        self.write(f"GAME OVER", move=False, align='center', font=('Courier', TEXT_SIZE, 'normal'))