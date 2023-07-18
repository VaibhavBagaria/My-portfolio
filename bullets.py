from turtle import *

class Bullets():
    def __init__(self):
        self.all_bullets=[]
        self.y_move=30
        self.player_x=0
        self.player_y=0
        self.charge_time=0
        
        
    def player_shoot(self):
        if self.charge_time==0:
            bullet=Turtle()
            bullet.shape('square')
            bullet.penup()
            bullet.color('white')
            bullet.shapesize(stretch_len=1, stretch_wid=0.1)
            bullet.setheading(90)
            bullet.goto(self.player_x, self.player_y+5)
            self.all_bullets.append(bullet)
            self.charge_time=4
            
        
        
    def move(self):
        for bullet in self.all_bullets:
            new_y=bullet.ycor()+self.y_move
            bullet.goto(bullet.xcor(), new_y)
        
    def start_charge_time(self):
        if self.charge_time > 0:
            self.charge_time-=1
            
    def destroy(self, bullet):
        bullet.goto(10000,10000)
        self.all_bullets.remove(bullet)
                
        
    
        