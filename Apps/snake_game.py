from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food - Food()

screen.listen()
screen.onkey(snake.up, "UP")
screen.onkey(snake.down, "DOWN")
screen.onkey(snake.left, "LEFT")
screen.onkey(snake.right, "RIGHT")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

   # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


    segments[0].forward(20)





screen.exitonclick()