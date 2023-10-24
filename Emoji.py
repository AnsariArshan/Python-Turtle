import turtle
import time


t = turtle.Turtle()
def semCircle():
    for i in range(200):
        t.right(1)
        t.fd(1)

def heart(size):
	t.pencolor("black")
	t.penup()
	t.goto(50,-150)
	t.pendown()
	t.fillcolor("red")
	t.begin_fill()
	t.left(95)
	t.fd(size)
	semCircle()
	t.left(135)
	semCircle()
	t.fd(size)
	t.end_fill()
time.sleep(2)

t.hideturtle()
t.penup()
t.goto(0,-200)
t.pendown()
t.pensize(5)
t.fillcolor("yellow")
t.begin_fill()
t.circle(200)
t.end_fill()

t.penup()
t.goto(-75,25)
t.pendown()
t.fillcolor("white")
t.begin_fill()
t.circle(50)
t.end_fill()
t.fillcolor("black")
t.penup()
t.goto(-50,50)
t.pendown()
t.begin_fill()
t.circle(12)
t.end_fill()


t.penup()
t.goto(75,25)
t.pendown()
t.fillcolor("white")
t.begin_fill()
t.circle(50)
t.end_fill()
t.penup()
t.goto(100,50)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(12)
t.end_fill()

t.penup()
t.goto(25,-150)
t.pendown()
t.circle(10,180)
t.left(180)
t.circle(10,180)
t.left(180)

heart(140)
time.sleep(5)