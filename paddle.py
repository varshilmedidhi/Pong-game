from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,cordinate):
        super().__init__()
        self.cordinates=cordinate
        self.shape('square')
        self.setposition(self.cordinates)
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)

    def forward(self):
        self.goto(self.xcor(), self.ycor() + 20)
    def backward(self):
        self.goto(self.xcor(), self.ycor() - 20)



