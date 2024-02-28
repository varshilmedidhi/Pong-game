from turtle import Turtle
import time
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.color('red')
        self.penup()
        self.speed('slow')
        self.xnew=10
        self.ynew=10
    def move(self):
        time.sleep(0.1)
        new_x=self.xcor()+self.xnew
        new_y=self.ycor()+self.ynew 
        self.goto(new_x,new_y)
    def detect_game_over(self):
        if self.pos()[0]>350:
            return True
        elif self.pos()[0]<-350:
            return True
    def detect_wall_collision(self):
        if self.ycor()>290 or self.ycor()<-290:
            return True
    def ball_bounce_y(self):
        self.ynew*=-1

    def detect_collision_with_paddle(self,turtle):
        if self.distance(turtle)<45 and self.xcor()>320:
            return True
        if self.distance(turtle)<45 and self.xcor()<-320:
            return True
    def ball_bounce_x(self):
        self.xnew*=-1
    def reset_ball(self):
        self.reset()
        self.shape('circle')
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color('red')
        self.penup()
        self.xnew*=-1
        self.ynew*=-1

