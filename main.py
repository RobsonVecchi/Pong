from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle
from random import choice

nums = list(range(0,31))
points = choice(nums)

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
ball = Ball()
ball.arise()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))




screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()

    if ball.distance(r_paddle) < 80 and ball.xcor() > 335:
        points = choice(nums)
        ball.reverse_x()



    if ball.distance(l_paddle) < 80 and ball.xcor() < -330:
        points = choice(nums)
        ball.reverse_y()



    if ball.xcor() > 350 or ball.xcor() < -350:
        points = choice(nums)
        ball.arise()



    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.reverse()





    

screen.exitonclick()
