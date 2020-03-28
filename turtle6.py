import turtle
import random

tut = turtle.Turtle()

tut.shape('turtle')
tut.color('green')
tut.width(6)

colors=['red', 'purple', 'blue', 'green', 'orange', 'yellow']

def up():
	tut.setheading(90)
	tut.forward(100)

def down():
	tut.setheading(270)
	tut.forward(100)

def right():
	tut.setheading(0)
	tut.forward(100)

def left():
	tut.setheading(180)
	tut.forward(100)

def color(x,y):
	tut.color(colors[random.randrange(1,len(colors))])

def clear(x,y):
	tut.clear()

turtle.listen()

turtle.onkey(up, 'w')
turtle.onkey(down, 's')
turtle.onkey(right, 'd')
turtle.onkey(left, 'a')

turtle.onscreenclick(color, 1)
turtle.onscreenclick(clear, 3)

turtle.mainloop()
