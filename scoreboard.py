from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 210)
        self.color("white")
        self.write(f"score = {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def update_score(self):

        self.clear()
        self.score += 1
        self.write(f"score = {self.score}", align='center', font=('Arial', 20, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", font=FONT)

