
from turtle import Turtle
DISTANCE = 20
COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.parts = []
        self.create_snake()
        # creating snake_head only after create_snake, otherwise parts[] will be empty, therefore, error
        self.snake_head = self.parts[0]

    # creating 3 squares, 20*20, as the snake's initial body

    def create_snake(self):
        for coordinate in COORDINATES:
            self.add_parts(coordinate)

        # print(body)

    def add_parts(self, coordinate):
        new_body = Turtle("square")
        new_body.color("white")
        new_body.penup()
        new_body.goto(coordinate)
        self.parts.append(new_body)

    # print(body)

    def extend_snake(self):
        self.add_parts(self.parts[-1].position())


    # moving the snake as: nth position occupying (n-1)th position

    def move(self):
        for i in range(len(self.parts) - 1, 0, -1):
            x = self.parts[i - 1].xcor()
            y = self.parts[i - 1].ycor()
            self.parts[i].goto(x, y)
        self.snake_head.forward(DISTANCE)

    def up(self):
        # heading() is used to determine the state of the turtle
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        # heading() is used to determine the state of the turtle
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def right(self):
        # heading() is used to determine the state of the turtle
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def left(self):
        # heading() is used to determine the state of the turtle
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)



