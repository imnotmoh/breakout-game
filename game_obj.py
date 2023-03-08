import random
from turtle import Turtle, Screen

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=6)
        self.shape("square")
        self.goto(x=0,y=-300)

    def move_right(self):
        if self.xcor() + 60 < 280:
            self.forward(20)

    def move_left(self):
        if self.xcor() - 60 > -280:
            self.backward(20)








class Blocks(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=2,stretch_wid=1)

color = ["red","yellow", "purple", "green", "blue", "pink", "brown"]

block_list = []
def arrangeblocks(screen_width, screen_height):
    x = -(screen_width/2) + 40
    y = (screen_height/2) - 20

    for i in range(int((screen_width - 40) /40) * 5):
        block_list.append(Blocks())
        block_list[i].goto(x,y)
        block_list[i].pensize(5)
        block_list[i].color("black")
        block_list[i].fillcolor(random.choice(color))

        x += 40
        if x > (screen_width/2) - 40:
            x = -(screen_width/2) + 40
            y -= 20


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("circle")
        self.penup()
        self.goto(random.randint(0,50), -280)
        self.setheading(random.randint(45,150))
        self.speed("fastest")


    def ball_physics(self):
        direction = self.heading()
        bounce_angle = 360 - direction
        self.setheading(bounce_angle)

    def wall_bounce_physics(self):
        direction = self.heading()
        bounce_angle = 180 - direction
        self.setheading(bounce_angle)

    def block_side_bounce(self):
        if self.heading() < 90 or self.heading() < 270:
            self.setheading(self.heading() + 45)
        elif self.heading() > 90 or self.heading() > 270:
            self.setheading(self.heading() - 45)









