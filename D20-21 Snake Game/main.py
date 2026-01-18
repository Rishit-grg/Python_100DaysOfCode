import turtle as t
import time
import snake
snake = snake.Snake()

screen = t.Screen()
screen.setup(600, 600)
screen.bgcolor("#93BC56")
screen.title("Snake Classic")
screen.tracer(0)

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.2)

    snake.move()

screen.exitonclick()