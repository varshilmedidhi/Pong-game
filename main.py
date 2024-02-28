import turtle
from turtle import  Turtle,Screen
from paddle import Paddle
from ball import Ball
import winsound
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.title('Pong game')
paddle_to_right=Paddle((350,0))
paddle_to_left=Paddle((-350,0))
balls=Ball()
game_on=True
left=0
right=0
right_turtle=Turtle()
left_turtle=Turtle()
while game_on:
    screen.listen()
    screen.onkeypress(paddle_to_right.forward, 'Up')
    screen.onkeypress(paddle_to_right.backward, 'Down')
    screen.onkeypress(paddle_to_left.forward, 'w')
    screen.onkeypress(paddle_to_left.backward, 's')
    balls.move()
    if balls.detect_game_over():
        if balls.xcor()<0:
            right+=1
            right_turtle.color('white')
            right_turtle.penup()
            right_turtle.goto(50,200)
            right_turtle.clear()
            right_turtle.write(f'{right}',False,'center',font=('Arial', 24, 'normal'))
            right_turtle.hideturtle()
        else:
            left+=1
            left_turtle.color('white')
            left_turtle.penup()
            left_turtle.goto(-50,200)
            left_turtle.clear()
            left_turtle.write(f'{left}', False, 'center', font=('Arial', 24, 'normal'))
            left_turtle.hideturtle()
        balls.reset_ball()
        continue
    if balls.detect_wall_collision():
        balls.ball_bounce_y()
        sound1 = winsound.PlaySound('cartoon-jump-6462.wav', winsound.SND_ASYNC)
    if balls.detect_collision_with_paddle(paddle_to_right) or balls.detect_collision_with_paddle(paddle_to_left):
        balls.ball_bounce_x()
        sound1 = winsound.PlaySound('cartoon-jump-6462.wav', winsound.SND_ASYNC)
screen.exitonclick()