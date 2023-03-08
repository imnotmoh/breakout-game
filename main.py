import time
from turtle import Turtle, Screen
from game_obj import *
my_screen = Screen()
my_screen.tracer(0)
my_screen.setup(width=600,height=700)
pace = 3
ball = Ball()

setup = ArrangedBlocks(ball)
setup.arrangeblocks(600,700)
# setup.block_list[5].goto(50,50)
pad = Paddle(ball)
game_is_on = True

block_list = []
while game_is_on:
    ball.forward(pace)
    setup.block_side_contact()
    setup.block_horizontal_contact()
    my_screen.update()
    # if ball.ycor() < -240:
    #     ball.ball_physics()
    if -265 < ball.xcor() < 280:
        pass
    else:
        ball.wall_bounce_physics()
    pad.contact()
    if ball.ycor() > 330:
        ball.ball_physics()
    elif ball.ycor() < - 360:
        ball.color("white")
        ball.__init__()

    my_screen.listen()
    my_screen.onkey(key="Right",fun=pad.move_right)
    my_screen.onkey(key="Left",fun=pad.move_left)
my_screen.mainloop()
