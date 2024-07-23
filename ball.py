from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.movement_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.movement_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1
        self.movement_speed *= 0.9

    def position_reset(self):
        self.goto(0, 0)
        self.movement_speed = 0.1
        self.bounce_x()