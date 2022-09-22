import turtle

wn = turtle.Screen()
wn.title("PingPongPython by David Morgenstern")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) # Stops the window from updating; speeds up the game

# Paddle A
paddle_A = turtle.Turtle()
paddle_A.speed(0)
paddle_A.shape("square")
paddle_A.color("white")
paddle_A.shapesize(stretch_wid=5, stretch_len=1)
paddle_A.penup()
paddle_A.goto(-350, 0)

# Paddle B
paddle_B = turtle.Turtle()
paddle_B.speed(0)
paddle_B.shape("square")
paddle_B.color("white")
paddle_B.shapesize(stretch_wid=5, stretch_len=1)
paddle_B.penup()
paddle_B.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.shapesize(stretch_wid=5, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

#

# Functions
def paddle_a_up():
    y = paddle_A.ycor()
    y += 20
    paddle_A.sety(y)

def paddle_a_down():
    y = paddle_A.ycor()
    y -= 20
    paddle_A.sety(y)

def paddle_b_up():
    y = paddle_B.ycor()
    y += 20
    paddle_B.sety(y)

def paddle_b_down():
    y = paddle_B.ycor()
    y -= 20
    paddle_B.sety(y)


# Keyboard Bindinb
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Main Game Loop
while True:
    wn.update()
    # turtle.done()

    # Moves the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0 , 0)
        ball.dx *= -1

    # Paddle & Ball Collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_B.ycor() + 40 and ball.ycor() > paddle_B.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_A.ycor() + 40 and ball.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
