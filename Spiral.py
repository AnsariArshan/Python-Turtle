import turtle
from time import sleep
import math

t = turtle.Turtle()
c = ["red","blue","green","yellow"]
j = 0
for i in range(10,0,-1):
	t.fillcolor(c[j])
	t.begin_fill()
	t.circle(i*10)
	t.end_fill()
	if (j<3):
		j +=1
	else:
		j = 0


sleep(2)