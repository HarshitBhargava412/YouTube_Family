import colorsys
from turtle import *

bgcolor("black")
speed(0)


n = 36
h = 0


for i in range(460):
    c = colorsys.hsv_to_rgb(h, 1, 0.9)
    h += 1/n
    
    color(c)
    left(145)
    
    for j in range(5):
        forward(300)
        left(150)