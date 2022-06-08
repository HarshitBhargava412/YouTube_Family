from turtle import *

speed(10)
bgcolor('white')
color('white')

penup()
goto(-80, 50)
pendown()

fillcolor("black")
begin_fill()
forward(200)
setheading(270)
s = 360

for i in range(9):
    s = s - 10
    setheading(s)
    forward(10)
    
forward(180)
s = 270
for i in range(9):
    s = s - 10
    setheading(s)
    forward(10)
    
forward(200)
s = 180
for i in range(9):
    s = s - 10
    setheading(s)
    forward(10)
    
forward(180)
s = 90
for i in range(9):
    s = s - 10
    setheading(s)
    forward(10)
    
forward(30)
end_fill()

penup()
color('black')
setheading(270)
forward(240)
setheading(0)
pendown()

color('red')
fillcolor("#E50914")

begin_fill()
forward(30)
setheading(90)
forward(180)
setheading(180)
forward(30)
setheading(270)
forward(180)
end_fill()

setheading(0)
penup()
forward(75)
pendown()
color('red')
fillcolor('#E50914')

begin_fill()
forward(30)
setheading(90)
forward(180)
setheading(180)
forward(30)
setheading(270)
forward(180)
end_fill()

color('red')
fillcolor('red')

begin_fill()
setheading(113)
forward(195)
setheading(0)
forward(31)
setheading(293)
forward(196)
end_fill()

hideturtle()
done()