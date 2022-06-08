import colorsys
from turtle import *

speed(0)
hideturtle()
goto(0, -100)

bgcolor("black")

h = 0
d = 200

p = True
n = 1

while 50:
    c = colorsys.hsv_to_rgb(h, 0.8, 0.4)
    h = h + 1/d
    color(c)
    circle(n)
    if p:
        n = n - 1
    else:
        n = n + 1
    
    if n == 0 or n == 60:
        p = not p
    left(1)
    forward(3)