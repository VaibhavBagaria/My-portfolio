from turtle import Turtle, register_shape
from random import randint

class Astroid():
    def __init__(self):
        self.all_astroids=[]
        
    def create_astroid(self):
        if randint(0,25)  == 15 and len(self.all_astroids) < 4:
            astroid=Turtle()
            shape = ((0, 0), (10, 10), (20, 0), (10, -10))
            register_shape('diamond', shape)
            astroid.shape('diamond')
            astroid.penup()
            astroid.shapesize(stretch_len=2, stretch_wid=2)
            astroid.color('brown')
            astroid.setheading(180)
            astroid.goto(randint(-300,300),290)
            self.all_astroids.append((astroid, randint(5,12)))
    
    def move(self):
        for astroid, y_move in self.all_astroids:
            new_y=astroid.ycor()-y_move
            astroid.goto(astroid.xcor(), new_y)
            
            
    def destroy(self, astroid):
        astroid[0].goto(10000,10000)
        self.all_astroids.remove(astroid)
        
            
        