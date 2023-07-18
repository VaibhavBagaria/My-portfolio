from turtle import Turtle

FONT=("Courier", 20, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setheading(90)
        self.score=0
        self.life=3
        self.x=0
        self.scoreboard()
    
    def scoreboard(self):
        self.color('red')
        for heart in range(0,self.life):
            self.goto(-350 + self.x, 250)
            self.write(f"❤", align='center', font=("Courier", 30, "normal"))
            self.x+=35
            
        self.color('white')
        self.goto(310, 250)
        self.write(f"Score: {self.score}", align='center', font=("Courier", 20, "normal"))
    
    def update_score(self):
        self.x=0
        self.clear()
        self.score+=10
        self.scoreboard()
        
    def update_life(self):
        self.x=0
        self.clear()
        self.life-=1
        self.scoreboard()
    
    def Game_Over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align='center', font=("Courier", 20, "bold"))
        
    
    