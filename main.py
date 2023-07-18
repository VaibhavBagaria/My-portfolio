import time
from turtle import *
from spaceship import Ship
from bullets import Bullets
from astroid import Astroid
from scoreboard import Score


screen = Screen()
screen.setup(width=800, height=600)
screen.title("Space Invaders")
screen.bgcolor("black")
screen.tracer(0)

ship=Ship()
astroids=Astroid()
bullets=Bullets()
scoreboard=Score()

screen.listen()
screen.onkeypress(ship.move_left, 'Left')
screen.onkeypress(ship.move_right, 'Right')
screen.onkeypress(bullets.player_shoot, 'space')

planet=Turtle()

planet.color('white')
planet.write(f"Save This Planet", align='center', font=("Courier", 20, "normal"))
time.sleep(3)
planet.clear()

planet.penup()
planet.shape("circle")
planet.shapesize(stretch_len=70 , stretch_wid=70)
planet.setheading(90)
planet.color('blue')
planet.goto(0,-920)

game_on=True
while game_on:
    time.sleep(0.1)
    screen.update()
    bullets.move()
    bullets.player_x=ship.xcor()
    bullets.player_y=ship.ycor()
    bullets.start_charge_time()
    astroids.create_astroid()
    astroids.move()
    for astroid, bullet in ((a,b) for a in astroids.all_astroids for b in bullets.all_bullets):
        if bullet.distance(astroid[0]) < 25:    
            bullets.destroy(bullet)
            astroids.destroy(astroid)
            scoreboard.update_score()
            
        if astroid[0].ycor() < -210:     
            print("hit")
            astroids.destroy(astroid)
            scoreboard.update_life()
            
        if ship.distance(astroid[0]) < 30:   
            print("hit")
            astroids.destroy(astroid)
            scoreboard.update_life()
    if scoreboard.life == 0:
        scoreboard.Game_Over()
            
screen.exitonclick()

























# ball=Ball()
# board=Board()

# #Move paddle/player
# screen.listen()
# screen.onkeypress(player.move_left,"Left")
# screen.onkeypress(player.move_right,"Right")

# heart=Turtle()
# heart.penup()
# heart.hideturtle()
# heart.setheading(90)
# heart.color('white')

# game_on=True
# while game_on:
#     time.sleep(ball.move_speed)
#     screen.update()
#     ball.move()
    
#     #Sense collision between ball and brick
#     for brick in brick_wall.all_bricks:
#         if ball.distance(brick) < 40:
#             brick_wall.destroy_brick(brick)
#             ball.bounce_y()
#             board.update_score()
                  
#     if player.distance(ball) < 50 and ball.ycor() < -220 :
#         ball.bounce_y()
        
#     if ball.ycor() > 580:
#         ball.bounce_y()
    
#     if ball.xcor() > 370 or ball.xcor() < -370:
#         ball.bounce_x()
        
#     if ball.ycor() < -290:
#         ball.spawn_point()
#         if ball.lives == 0:
#             board.game_over()
#             break
        
#     hearts=''
#     for life in range(0,ball.lives):
#         hearts+='❤'
#     heart.clear()
#     heart.goto(-350,-230)
#     heart.write(f"{hearts}",align="center",font=("Courier", 20, "normal"))
        
    
# screen.exitonclick()