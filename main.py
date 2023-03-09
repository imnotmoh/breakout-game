import time
from turtle import Turtle, Screen
from game_obj import *
# player livees
lives = 5
# gamee pace
pace = 5
# creating our game objects
my_screen = Screen()
my_screen.bgcolor("black")
my_screen.tracer(0)
my_screen.setup(width=600, height=700)
ball = Ball()
setup = ArrangedBlocks(ball)
setup.arrangeblocks(600, 700)
pad = Paddle(ball)
game_is_on = True
block_list = []
while game_is_on:

    time.sleep(ball.speed_)
    ball.forward(pace)
    setup.block_side_contact()
    setup.block_horizontal_contact()
    my_screen.update()
    # if ball.ycor() < -240:
    #     ball.ball_physics()
    if -270 < ball.xcor() < 280:
        pass
    else:
        ball.wall_bounce_physics()
    pad.contact()
    if ball.ycor() > 330:
        ball.ball_physics()
    elif ball.ycor() < - 360:
        ball.color("white")
        if lives > 0:
            ball.__init__()
            lives -= 1
        else:
            game_over = GameOver()
            break

    if len(setup.block_list) < 1:
        setup.level += 1
        setup.arrangeblocks(600, 700)

    my_screen.listen()
    my_screen.onkey(key="Right", fun=pad.move_right)
    my_screen.onkey(key="Left", fun=pad.move_left)
my_screen.mainloop()
