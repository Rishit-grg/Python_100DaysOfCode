import turtle as t
import time
import snake
import food
import score
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

food = food.Food()
score = score.Score()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.2)

    snake.move()
    if snake.head.distance(food) < 21  :
        score.goto(y=270, x=0)
        score.update_score()
        food.newpos()




screen.exitonclick()