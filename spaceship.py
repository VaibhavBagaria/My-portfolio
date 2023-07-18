from turtle import *

STARTING_POSITION = (10, -200)

class Ship(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("triangle")
        self.color('aqua')
        self.shapesize(stretch_len=2 , stretch_wid=2)
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.move_speed=30
        
    def move_left(self):
        if self.xcor() >= -300:
            self.goto(self.xcor()-self.move_speed, self.ycor())
        
    def move_right(self):
        if self.xcor() <= 300:
            self.goto(self.xcor()+self.move_speed, self.ycor())
            