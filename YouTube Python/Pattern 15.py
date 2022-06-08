from turtle import *

bgcolor("black")
speed(0)
setup(1960, 1080, 0, 0)

penup()
left(90)
goto(0, 0)
forward(100)
left(180)
pendown()
j = 0

for rings in range(2):
    pencolor("red")
    for i in range(150):
        forward(100)
        left(111)
    penup()
    right(90 * j)
    pendown()
    
    pencolor("dark blue")
    for i in range(150):
        forward(102)
        right(111)
    penup()
    right(180 * j)
    pendown()
    
    pencolor("dark violet")
    for i in range(150):
        forward(104)
        left(111)
    penup()
    right(90 * j)
    pendown()
    
    pencolor("dark red")
    for i in range(150):
        forward(106)
        right(111)
    penup()
    right(180 * j)
    pendown()
    
    pencolor("dark orange")
    for i in range(150):
        forward(104)
        left(111)
    penup()
    right(90 * j)
    pendown()
    
    pencolor("dark blue")
    for i in range(150):
        forward(102)
        right(111)
    penup()
    right(180 * j)
    pendown()
    
    pencolor("dark grey")
    for i in range(150):
        forward(100)
        left(111)
    penup()
    right(90 * j)
    pendown()
    
    pencolor("red")
    for i in range(150):
        forward(100)
        left(111)
    penup()
    right(90 * j)
    pendown()
    
    pencolor("dark blue")
    for i in range(150):
        forward(102)
        right(111)
    penup()
    right(180 * j)
    pendown()
    
    pencolor("dark violet")
    for i in range(150):
        forward(104)
        left(111)
    penup()
    right(90 * j)
    pendown()
    
    pencolor("dark red")
    for i in range(150):
        forward(106)
        right(111)
    penup()
    right(180 * j)
    pendown()
    
    pencolor("dark orange")
    for i in range(150):
        forward(104)
        left(111)
    penup()
    right(90 * j)
    pendown()
    
    pencolor("dark blue")
    for i in range(150):
        forward(102)
        right(111)
    penup()
    right(180 * j)
    pendown()
    
    pencolor("dark grey")
    for i in range(150):
        forward(100)
        left(111)
    penup()
    right(90 * j)
    pendown()
    
done()
