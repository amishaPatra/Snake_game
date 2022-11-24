from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.title("Welcome to the Snake Game")
screen.tracer(0)


new_snake = Snake()
food = Food()
scoreboard = Scoreboard()


# giving access to keyboard
screen.listen()
screen.onkey(new_snake.up, "Up")
screen.onkey(new_snake.down, "Down")
screen.onkey(new_snake.right, "Right")
screen.onkey(new_snake.left, "Left")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    new_snake.move()

    if new_snake.snake_head.distance(food) < 15:
        # Detect collision with food
        # distance(x,y) method compares the distance coordinates from the the turtle's coordinates
        food.refresh_location()
        new_snake.extend_snake()
        scoreboard.update_score()

    # Detect collision with the wall
    if new_snake.snake_head.xcor() > 250 or new_snake.snake_head.xcor() < -250 or new_snake.snake_head.ycor() > 250 or new_snake.snake_head.ycor() < -250:
        game_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for body in new_snake.parts:
        if body == new_snake.snake_head:
            pass
        elif new_snake.snake_head.distance(body) < 10:
            game_on = False
            scoreboard.game_over()


screen.exitonclick()
