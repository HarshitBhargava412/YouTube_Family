import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')

t.speed(95)

n = 300
h = 0

for i in range(360):
    t.color(h, 1, 0.8)
    
    h += 1/n
    
    t.left(2)
    t.forward(i * 2)
    t.right(150)
    
    for j in range(3):
        t.right(5)
        t.forward(10)
        t.left(150)