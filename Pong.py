import turtle as t
import os

score = 0
MAX_BALL_X_SPEED = 0.2
MAX_BALL_Y_SPEED = 0.2


window = t.Screen()
window.title("The Pong Game")
window.bgcolor("light green")
window.setup(width=800, height=600)
window.tracer(0)

#setting up paddle colors
leftpaddle = t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("dark green")
leftpaddle.shapesize(stretch_wid=5, stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350, 0)

#setting up ball colors
ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("violet")
ball.penup()
ball.goto(5, 5)
ballxdirection = 0.2
ballydirection = 0.2

#setting score colors
pen = t.Turtle()
pen.speed(0)
pen.color("#000000")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0", align="center", font=('Spectral', 24, 'normal'))

# movement of paddle
def leftpaddleup():
    y = leftpaddle.ycor()
    y += 40
    if y > 250:
        y = 250
    leftpaddle.sety(y)

def leftpaddledown():
    y = leftpaddle.ycor()
    y -= 40
    if y < -250:
        y = -250
    leftpaddle.sety(y)

# Assign keys to play
window.listen()
window.onkeypress(leftpaddleup, 'w')
window.onkeypress(leftpaddledown, 's')

while True:
    window.update()

    # Cap the ball's x and y speed
    if abs(ballxdirection) > MAX_BALL_X_SPEED:
        ballxdirection = MAX_BALL_X_SPEED * (ballxdirection / abs(ballxdirection))

    if abs(ballydirection) > MAX_BALL_Y_SPEED:
        ballydirection = MAX_BALL_Y_SPEED * (ballydirection / abs(ballydirection))

    # Move the ball
    ball.setx(ball.xcor() + ballxdirection)
    ball.sety(ball.ycor() + ballydirection)

    # Border set up
    if ball.ycor() > 290:
        ball.sety(290)
        ballydirection = ballydirection * -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ballydirection = ballydirection * -1

    if ball.xcor() > 390:
        ball.goto(390, ball.ycor())
        ballxdirection = ballxdirection * -1
        os.system("afplay wallhit.wav&")

    if ball.xcor() < -390:  # Adjusted the x-coordinate condition
        pen.clear()
        pen.write("Game Over", align="center", font=('Monaco', 24, "normal"))
        ball.goto(0, 0)
        ballxdirection *= -2
        score = 0
        pen.clear()
        pen.write("Score: 0", align="center", font=('Monaco', 24, "normal"))

    # Handling the collision with the left paddle
    if (-360 <= ball.xcor() <= -340) and (leftpaddle.ycor() - 50 < ball.ycor() < leftpaddle.ycor() + 50):
        ball.setx(-340)
        ballxdirection = ballxdirection * -1
        os.system("afplay paddle.wav&")

        # make the ball bounce back when it hits the paddle
        bally_offset = ball.ycor() - leftpaddle.ycor()
        ballydirection = bally_offset / 50

        score += 1
        pen.clear()
        pen.write("Score: {}".format(score), align="center", font=('Spectral', 24, "normal"))
    
    # Game winner
    if score >= 5:
        pen.clear()
        pen.write("You Win!", align="center", font=('Monaco', 24, "normal"))
        ball.goto(0, 0)
        ballxdirection = 0 
        ballydirection = 0

