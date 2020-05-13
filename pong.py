import turtle

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)
score_a = 0

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)
score_b = 0


# Ball
color = ("white", "green", "orange", "red", "pink", "blue", "purple", "cyan")
color_index = 0
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color(color[color_index])
ball.goto(0,0)
ball.penup()
ball.dx = 0.3
ball.dy = 0.3

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: " + str(score_a) + "\tPlayer B: " + str(score_b), align="center", font=("Courier", 24, "normal"))



def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")


# Main game loop

while True:
    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        score_a += 1
        pen.clear()
        pen.write("Player A: " + str(score_a) + "\tPlayer B: " + str(score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
    if ball.xcor() < -390:
        score_b += 1
        pen.clear()
        pen.write("Player A: " + str(score_a) + "\tPlayer B: " + str(score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    if (ball.xcor() > 340 and ball.xcor() < 350)\
         and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.dx *= -1
        if color_index == len(color)-1:
            color_index = 0
        ball.color(color[color_index])
        color_index += 1
        continue
    
    if (ball.xcor() < -340 and ball.xcor() > -350)\
         and (ball.ycor() > paddle_a.ycor() - 40 and ball.ycor() < paddle_a.ycor() + 40):
        ball.dx *= -1
        if color_index == len(color)-1:
            color_index = 0
        ball.color(color[color_index])
        color_index += 1
        continue
    




