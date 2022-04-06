from turtle import *

bgcolor('black')

speed(0)

n = 300
h = 0

for i in range(360):
    color(h, 0.5, 1)
    
    h += 1/n
    
    left(2)
    forward(i * 2)
    right(150)
    
    for j in range(3):
        right(2)
        forward(4)
        done()

