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

# Ball

# Main Game Loop
while True:
    wn.update()