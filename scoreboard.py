from turtle import  Turtle
class Scoreboard(Turtle):
    def __int__(self):
        super().__int__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.ls=0
        self.rs=0