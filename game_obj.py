import random
from turtle import Turtle, Screen

pace = 0

class Paddle(Turtle):
    def __init__(self, ball):
        super().__init__()
        self.ball = ball
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=6)
        self.shape("square")
        self.color("white")
        self.goto(x=0, y=-300)

    def move_right(self):
        if self.xcor() + 60 < 280:
            self.forward(20)

    def move_left(self):
        if self.xcor() - 60 > -280:
            self.backward(20)

    def contact(self):
        if self.ycor() + 15 >= self.ball.ycor() >=self.ycor():
            if self.xcor() - 60 <= self.ball.xcor() <= self.xcor():
                self.ball.setheading(90 -(-self.xcor() + self.ball.xcor()))
                if self.ball.speed_ > 0:
                    self.ball.speed_ -= 0.001
            if self.xcor() + 60 >= self.ball.xcor() >= self.xcor():
                self.ball.setheading(90 -(-self.xcor() + self.ball.xcor()))
                if self.ball.speed_ > 0:
                    self.ball.speed_ -= 0.001




class Blocks(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)


color = ["red", "yellow", "purple", "green", "blue", "pink", "brown"]


class ArrangedBlocks():
    def __init__(self, ball):
        self.block_list = []
        self.ball = ball
        self.level = 1

    def arrangeblocks(self, screen_width, screen_height):

        x = -(screen_width / 2) + 40
        y = (screen_height / 2) - 20

        for i in range(int((screen_width - 40) / 40) * (4+self.level)):
            self.block_list.append(Blocks())
            self.block_list[i].goto(x, y)
            self.block_list[i].pensize(5)
            self.block_list[i].color("black")
            self.block_list[i].fillcolor(random.choice(color))

            x += 40
            if x > (screen_width / 2) - 40:
                x = -(screen_width / 2) + 40
                y -= 20

    def block_horizontal_contact(self):
        global speed
        for block in self.block_list:
            if block.ycor() - 15 <= self.ball.ycor() <= block.ycor():
                pos_prox = block.xcor() - self.ball.xcor()
                if -20 <= pos_prox <= 20:
                    block.hideturtle()
                    if self.ball.speed_ > 0:
                        self.ball.speed_ -= 0.001
                    self.block_list.remove(block)
                    self.ball.ball_physics()
                    self.ball.forward(pace)


            if block.ycor() + 15 >= self.ball.ycor() >= block.ycor():
                pos_prox = block.xcor() - self.ball.xcor()
                if -20 <= pos_prox <= 20:
                    block.hideturtle()
                    self.block_list.remove(block)
                    self.ball.ball_physics()
                    self.ball.forward(pace)
                    if self.ball.speed_ > 0:
                        self.ball.speed_ -= 0.001
                    return True

    def block_side_contact(self):
        global speed
        for block in self.block_list:
            if block.ycor() - 10 < self.ball.ycor() < block.ycor() + 10:
                if block.xcor() + 21 > self.ball.xcor() > block.xcor() and block.distance(self.ball) < 26:
                    block.hideturtle()
                    self.block_list.remove(block)
                    self.ball.wall_bounce_physics()
                    self.ball.forward(pace)
                    if self.ball.speed_ > 0:
                        self.ball.speed_ -= 0.001
                elif block.xcor() - 21 < self.ball.xcor() < block.xcor() and block.distance(self.ball) < 26:
                    block.hideturtle()
                    self.block_list.remove(block)
                    self.ball.wall_bounce_physics()
                    self.ball.forward(pace)
                    if self.ball.speed_ > 0:
                        self.ball.speed_ -= 0.001


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.goto(0, -300)
        self.setheading(random.randint(45, 150))
        self.speed_ = 0.01
        self.speed(0)

    def ball_physics(self):
        direction = self.heading()
        bounce_angle = 360 - direction
        self.setheading(bounce_angle)

    def wall_bounce_physics(self):
        direction = self.heading()
        bounce_angle = 180 - direction
        self.setheading(bounce_angle)



class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0,0)
        self.color("white")
        self.write("gameover")
