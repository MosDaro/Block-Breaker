import turtle

class Window:
    def __init__(self, title, bg):
        self.turtle = turtle.Screen()
        self.turtle.title(title)
        self.turtle.bgcolor(bg)
        self.turtle.setup(width=600, height=600)
        self.turtle.tracer(0)

class Paddle:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.shape("square")
        self.turtle.color("white")
        self.turtle.shapesize(1, 5)
        self.turtle.penup()
        self.turtle.goto(0, -230)


class Ball:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.shape("circle")
        self.turtle.color("white")
        self.turtle.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.turtle.penup()
        self.turtle.goto(0,0)
        self.turtle.dx = 2
        self.turtle.dy = 2
        


class Score:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.color("white")
        self.turtle.penup()
        self.turtle.hideturtle()
        self.turtle.goto(-290, 280)
        self.turtle.sc = 0
    def increase_score(self,score):
        score.turtle.sc += 1


class Life:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.color("white")
        self.turtle.penup()
        self.turtle.hideturtle()
        self.turtle.goto(-290, 260)
        self.turtle.life = 3

class Block:
    def __init__(self, location, shape , size, frame_color, fill_color, matireal):
        self.turtle = turtle.Turtle()
        self.turtle.penup()
        self.turtle.goto(location)
        self.turtle.shape(shape)
        self.turtle.shapesize(stretch_len=size[0], stretch_wid=size[1])
        self.turtle.color(frame_color, fill_color)
        self.turtle.begin_fill()
        self.turtle.life = matireal
        self.turtle.end_fill()

