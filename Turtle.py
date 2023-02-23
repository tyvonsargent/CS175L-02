import math
import turtle

WINDOW_Width = 400
WINDOW_Height = 400
ANIMATION_Speed = 0
NUM_SIDES = 8 
LENGTH = 100
ANGLE = 45
TEXT_X = -5
TEXT_Y = -10

turtle.setup(WINDOW_Width,WINDOW_Height)

S = LENGTH
X = S/math.sqrt(2)
diameter = S + (2 * X)

screen = turtle.Screen()
screen.bgcolor('black')

t = turtle.Turtle()

t.shape('turtle')

t.penup()
t.goto(-50, 100)
t.pendown()
t.color('white', 'red')
t.begin_fill()
for i in range(NUM_SIDES):
    t.forward(LENGTH)
    t.right(ANGLE)

t.end_fill()

t.penup()
t.right(90)
t.forward(140)
t.color('white')
t.write('STOP', font = ('Arial', 30, 'normal'))
        
t.hideturtle()
