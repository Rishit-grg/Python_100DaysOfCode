import turtle
import time
import snake
import food
import score


snake = snake.Snake()


screen = turtle.Screen()
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
score.goto(y=270, x=0)

# Game Loop
game_on = True
while game_on:
    screen.update()
    time.sleep(0.15)

    if score.score == 0:
        score.show_score()

    snake.move()

    if snake.head.distance(food) < 21  :
        score.update_score()
        food.new_posn()
        snake.grow()

    for segment in snake.snake[1::]:
        if snake.head.distance(segment) < 15:
            score.check_highscore()
            score.goto(y=0, x=0)
            score.game_over()
            game_on = False

    if snake.head.xcor()>300 or snake.head.xcor() <-300:
        snake.head.goto(-snake.head.xcor(),snake.head.ycor())

    if snake.head.ycor() > 300 or snake.head.ycor() < -300:
        score.check_highscore()
        score.goto(y=0, x=0)
        score.game_over()
        game_on = False

screen.exitonclick()
