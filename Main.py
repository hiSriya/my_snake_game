from turtle import Turtle, Screen

from Food import Food
from scoreboard import ScoreBoard
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0.75)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_tail()
        scoreboard.increase_score()
    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        scoreboard.reset_scoreboard()
        snake.reset_snake()
    # detect collision with tail
    for seg in snake.segment[1:]:
        if snake.head.distance(seg) < 10:
            scoreboard.reset_scoreboard()
            snake.reset_snake()

screen.exitonclick()
