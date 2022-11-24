from turtle import Turtle
import random

# Food class inherited from the Turtle class

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # shapesize() to change the pixels of the turtle which is a circle in this case
        self.shapesize()
        self.color("pale green")
        self.speed(10)
        self.refresh_location()

    def refresh_location(self):

        x = random.randint(-230, 230)
        y = random.randint(-230, 230)
        self.goto(x, y)



