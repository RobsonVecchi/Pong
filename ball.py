from turtle import Turtle
from random import choice

HEADINGS = [0, 20, 40, 60, 120, 140, 160, 180, 200, 220, 240, 320, 340]
R_HEADINGS = [110,160, 210, 250]
L_HEADINGS = [70, 20, 330, 290]
    #list(range(0, 360, 20))


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("navy")
        self.penup()


    def reverse(self):
        heading = self.heading()
        new_heading = heading*-1
        self.setheading(new_heading)

    def reverse_x(self):
        self.setheading(choice(R_HEADINGS))

    def reverse_y(self):
        self.setheading(choice(L_HEADINGS))


    def arise(self):
        self.goto(0,0)
        self.setheading(choice(HEADINGS))


    def move(self):
        self.forward(1)
