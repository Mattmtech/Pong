import turtle

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Left Paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)

#Right Paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .2
ball.dy = -.2

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 255)
pen.write("Player 1: 0  Player 2: 0", align = "center", font = ("Courier", 24, "normal"))

#Functions
def left_paddle_up():
    y = left_paddle.ycor()
    y+=20
    left_paddle.sety(y)
def left_paddle_down():
    y = left_paddle.ycor()
    y-=20
    left_paddle.sety(y)

def right_paddle_up():
    y = right_paddle.ycor()
    y+=20
    right_paddle.sety(y)

def right_paddle_down():
    y = right_paddle.ycor()
    y-=20
    right_paddle.sety(y)

#Key Listeners
window.listen()
window.onkeypress(left_paddle_up, "w")
window.onkeypress(left_paddle_down, "s")
window.onkeypress(right_paddle_up, "Up")
window.onkeypress(right_paddle_down, "Down")

p1_score = 0
p2_score = 0
while True:
    window.update()

    #move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #boundary checking for the ball
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        p1_score += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(p1_score, p2_score), align="center",
                  font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
    if ball.xcor() < -390:
        p2_score += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(p1_score, p2_score), align="center",
                  font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
    #Setting boundaries for the paddles
    if right_paddle.ycor() > 250:
        right_paddle.goto(right_paddle.xcor(), 250)
    if right_paddle.ycor() < -250:
        right_paddle.goto(right_paddle.xcor(), -250)
    if left_paddle.ycor() > 250:
        left_paddle.goto(left_paddle.xcor(), 250)
    if left_paddle.ycor() < -250:
        left_paddle.goto(left_paddle.xcor(), -250)



    #Paddle Collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < right_paddle.ycor() + 50 and ball.ycor() > right_paddle.ycor() -50):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < left_paddle.ycor() + 50 and ball.ycor() > left_paddle.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1








