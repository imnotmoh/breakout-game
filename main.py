import time
from turtle import Turtle, Screen
from game_obj import *
my_screen = Screen()
my_screen.tracer(0)
my_screen.setup(width=600,height=700)
arrangeblocks(600,700)
ball = Ball()
pad = Paddle()
game_is_on = True
while game_is_on:
    time.sleep(0.0001)
    for block in block_list:
        try:
            if ball.distance(block) < 35 and block.ycor() - 35 < ball.ycor():
                if 20 < block.distance(block_list[block_list.index(block) + 1]) > 40 or 20 < block.distance(block_list[block_list.index(block) - 1]) > 40:
                    print(1)
                    if (ball.distance(block) < 20 and block.xcor() + 20 > ball.xcor()) or (ball.distance(block) < 20 and block.xcor() - 20 < ball.xcor()):
                        print(2)
                        if ball.ycor() + 5 > block.ycor():
                            print("hello")
                            ball.block_side_bounce()
                            ball.forward(10)
                            block.hideturtle()
                            block_list.remove(block)
                    else:
                        ball.ball_physics()
                        ball.forward(10)
                        block_list.remove(block)
                        block.hideturtle()
                        print("na me")
                else:
                    ball.ball_physics()
                    ball.forward(10)
                    block_list.remove(block)
                    block.hideturtle()
                    print("na me")
        except IndexError:


            if ball.distance(block) < 25 and block.ycor() - 25 < ball.ycor():
                ball.ball_physics()
                ball.forward(10)
                block_list.remove(block)
                block.hideturtle()
            elif 20 < block.distance(block_list[block_list.index(block) - 1]) > 40:
                if (ball.distance(block) < 25 and block.xcor() - 25 < ball.ycor()) or (ball.distance(block) < 25 and block.xcor() + 25 > ball.ycor()):
                    ball.block_side_bounce()
                    ball.forward(10)
                    block.hideturtle()
                    block_list.remove(block)

    if pad.ycor() + 10 > ball.ycor() and ball.distance(pad) < 60:
        if ball.ycor() > pad.ycor():
            ball.ball_physics()
    if ball.xcor() > 280 or ball.xcor() < - 280:
        ball.wall_bounce_physics()
    if ball.ycor() > 330:
        ball.ball_physics()
    ball.forward(5)
    my_screen.update()
    if ball.ycor() < -330:
        ball.goto(0,-400)
        ball.__init__()
    my_screen.listen()
    my_screen.onkey(key="Right",fun=pad.move_right)
    my_screen.onkey(key="Left",fun=pad.move_left)
my_screen.mainloop()
