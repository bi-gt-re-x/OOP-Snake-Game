from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time
import scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
foods = Food()
score = Score()

def move_snake():
    time.sleep(0.1)
    screen.update()
    snake.move()

game_is_on = True
while game_is_on:
    screen.listen()
    while screen.onkey(snake.up, "Up"):
        snake.up()
    while screen.onkey(snake.down, "Down"):
        snake.down()
    while screen.onkey(snake.left, "Left"):
        snake.left()
    while screen.onkey(snake.right, "Right"):
        snake.right()
    move_snake()
    snake.movers()

    #This part was notoriously difficult; it took me 20 min just to think of an idea so the snake won't kill itself when the head is touching the second node.

    if snake.segments[0].distance(foods) < 15:
        foods.refresh()
        snake.extend()
        scoreboard.score += 1
        score.reset_score()
        score = Score()

    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290:
        score.reset_game()
        snake.reset()

    elif snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < -290:
        score.reset_game()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            score.reset_game()
            snake.reset()

screen.exitonclick()
