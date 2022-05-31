from turtle import *

speed(0)


def draw():
    for i in range(4):
        forward(30)
        left(90)
        
    forward(30)
    

for j in range(8):
    up()
    setposition(-150, 30 * j)
    down()
    
    for k in range(4):
        
        if j % 2 == 0:
            fillcolor("black")
            begin_fill()
            draw()
            end_fill()
            
            fillcolor("white")
            begin_fill()
            draw()
            end_fill()
        else:
            fillcolor("white")
            begin_fill()
            draw()
            end_fill()
    
            fillcolor("black")
            begin_fill()
            draw()
            end_fill()
        
        
hideturtle()
done()