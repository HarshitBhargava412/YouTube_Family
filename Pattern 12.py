from turtle import *

bgcolor("black")
speed(0)
hideturtle()
pattern_colors = ["white", "red"]

for i in range(180):
    color(pattern_colors[i % len(pattern_colors)])
    right(i)
    circle(100, i)
    forward(i)
    right(180)
    forward(i)
    
done()
