import turtle
from time import sleep
t = turtle.Turtle()


t.hideturtle()
t.pensize(10)


t.penup()
t.goto(0,-200)
t.pendown()


#Making the circle
t.fillcolor("red")
t.begin_fill()
t.circle(200)
t.end_fill()

#making outer 'A'
t.fillcolor("Green")
t.begin_fill()
t.penup()
t.goto(-90,-170)
t.pendown()
t.goto(-120,-250)
t.left(180)
t.fd(60)
t.goto(-30,200)
t.left(180)
t.fd(60)
t.goto(60,-200)
t.left(180)
t.fd(60)
t.goto(0,-170)
t.goto(-90,-170)
t.end_fill()


#Making inner 'A'
t.fillcolor("red")
t.begin_fill()
t.penup()
t.goto(-67,-110)
t.pendown()

t.left(180)
t.fd(60)
t.goto(-10,12)
t.left(180)
t.fd(30)
t.goto(-67,-110)
t.end_fill()

#Writing AVENGERS
t.penup()
t.goto(-240,210)
t.pendown()
t.write("AVENGERS ASSEMBLE",font=("Arial", 30, "normal"))

sleep(10)
