import turtle as t

class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]


    def create_snake(self):
        for pos in [(0, 0), (-20, 0), (-40, 0)]:
            segment = t.Turtle("square")
            segment.color("#587CFF")
            self.snake.append(segment)
            segment.pu()
            segment.goto(pos)

    def move(self):
        for seg_num in range(-1, -(len(self.snake)), -1):
            x = self.snake[seg_num - 1].xcor()
            y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(x, y)
        self.snake[0].forward(20)


    def move_left(self):
        if self.head.heading() != 0:
            self.snake[0].setheading(180)

    def move_right(self):
        if self.head.heading() != 180:
            self.snake[0].setheading(0)

    def move_up(self):
        if self.head.heading() != 270:
            self.snake[0].setheading(90)

    def move_down(self):
        if self.head.heading() != 90:
            self.snake[0].setheading(270)
