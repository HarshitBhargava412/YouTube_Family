from turtle import *

pensize(3)
speed(9)


def myposition(x, y):
    penup()
    goto(x, y)
    pendown()
    
    
def leftEye(x, y):
    myposition(x, y)
    setheading(0)
    fillcolor('#333333')
    begin_fill()
    circle(22)
    end_fill()
    
    myposition(x, y + 10)
    fillcolor('#000000')
    begin_fill()
    circle(10)
    end_fill()
    
    myposition(x + 6, y + 22)
    fillcolor('#ffffff')
    begin_fill()
    circle(10)
    end_fill()


def rightEye(x, y):
    myposition(x, y)
    setheading(0)
    fillcolor('#333333')
    begin_fill()
    circle(22)
    end_fill()
    
    myposition(x, y + 10)
    fillcolor('#000000')
    begin_fill()
    circle(10)
    end_fill()
    
    myposition(x - 6, y + 22)
    fillcolor('#ffffff')
    begin_fill()
    circle(10)
    end_fill()


def mouth(x, y):
    myposition(x, y)
    fillcolor('#88141D')
    begin_fill()
    
    # Lower Lip
    l1 = []
    l2 = []
    setheading(190)
    a = 0.7
    for i in range(28):
        a += 0.1
        right(3)
        fd(a)
        l1.append(position())
    
    myposition(x, y)
    setheading(10)
    a = 0.7
    for i in range(28):
        a += 0.1
        left(3)
        fd(a)
        l2.append(position())
    
    # Upper Lip
    setheading(10)
    circle(50, 15)
    left(180)
    circle(-50, 15)
    
    circle(-50, 40)
    setheading(233)
    circle(-50, 55)
    left(180)
    circle(50, 12.1)
    end_fill()
    
    # Tongue
    myposition(17, 54)
    fillcolor('#DD716F')
    begin_fill()
    setheading(145)
    circle(40, 86)
    penup()
    for pos in reversed(l1[:20]):
        goto(pos[0], pos[1] + 1.5)
    
    for pos in l2[:20]:
        goto(pos[0], pos[1] + 1.5)
    pendown()
    end_fill()
    
    # Nose
    myposition(-17, 94)
    setheading(8)
    fd(4)
    back(8)

# Red Cheeks
def leftCheek(x, y):
    myposition(x, y)
    setheading(300)
    fillcolor('#DD4D28')
    begin_fill()
    a = 2.3
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a -= 0.05
            lt(3)
            fd(a)
        else:
            a += 0.05
            lt(3)
            fd(a)
    end_fill()


def rightCheek(x, y):
    myposition(x, y)
    setheading(60)
    fillcolor('#DD4D28')
    begin_fill()
    a = 2.3
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a -= 0.05
            lt(3)
            fd(a)
        else:
            a += 0.05
            lt(3)
            fd(a)
    end_fill()


def colorLeftEar(x, y):
    myposition(x, y)
    fillcolor('#000000')
    begin_fill()
    setheading(330)
    circle(100, 35)
    setheading(219)
    circle(-300, 19)
    setheading(110)
    circle(-30, 50)
    circle(-300, 10)
    end_fill()


def colorRightEar(x, y):
    myposition(x, y)
    fillcolor('#000000')
    begin_fill()
    setheading(300)
    circle(-100, 30)
    setheading(35)
    circle(300, 15)
    circle(30, 50)
    setheading(190)
    circle(300, 17)
    end_fill()


def body():
    fillcolor('#F6D02F')
    begin_fill()
    # Right face contour
    penup()
    circle(130, 40)
    pendown()
    circle(100, 105)
    left(180)
    circle(-100, 5)
    
    # Right ear
    setheading(20)
    circle(300, 30)
    circle(30, 50)
    setheading(190)
    circle(300, 36)
    
    # Upper profile
    setheading(150)
    circle(150, 70)
    
    # Left ear
    setheading(200)
    circle(300, 40)
    circle(30, 50)
    setheading(20)
    circle(300, 35)
    
    # Left face contour
    setheading(240)
    circle(105, 95)
    left(180)
    circle(-105, 5)
    
    # Left hand
    setheading(210)
    circle(500, 18)
    setheading(200)
    fd(10)
    setheading(280)
    fd(7)
    setheading(210)
    fd(10)
    setheading(300)
    circle(10, 80)
    setheading(220)
    fd(10)
    setheading(300)
    circle(10, 80)
    setheading(240)
    fd(12)
    setheading(0)
    fd(13)
    setheading(240)
    circle(10, 70)
    setheading(10)
    circle(10, 70)
    setheading(10)
    circle(300, 18)
    
    setheading(75)
    circle(500, 8)
    left(180)
    circle(-500, 15)
    setheading(250)
    circle(100, 65)
    
    # Left foot
    setheading(320)
    circle(100, 5)
    left(180)
    circle(-100, 5)
    setheading(220)
    circle(200, 20)
    circle(20, 70)
    
    setheading(60)
    circle(-100, 20)
    left(180)
    circle(100, 20)
    setheading(300)
    circle(10, 70)
    
    setheading(60)
    circle(-100, 20)
    left(180)
    circle(100, 20)
    setheading(10)
    circle(100, 60)
    
    # Horizontal
    setheading(180)
    circle(-100, 10)
    left(180)
    circle(100, 10)
    setheading(5)
    circle(100, 10)
    circle(-100, 40)
    circle(100, 35)
    left(180)
    circle(-100, 10)
    
    # Right foot
    setheading(290)
    circle(100, 55)
    circle(10, 50)
    
    setheading(120)
    circle(100, 20)
    left(180)
    circle(-100, 20)
    
    setheading(0)
    circle(10, 50)
    
    setheading(110)
    circle(100, 20)
    left(180)
    circle(-100, 20)
    
    setheading(30)
    circle(20, 50)
    
    setheading(100)
    circle(100, 40)
    
    # Right body contour
    setheading(200)
    circle(-100, 5)
    left(180)
    circle(100, 5)
    left(30)
    circle(100, 75)
    right(15)
    circle(-300, 21)
    left(180)
    circle(300, 3)
    
    # Right hand
    setheading(43)
    circle(200, 60)
    
    right(10)
    fd(10)
    
    circle(5, 160)
    setheading(90)
    circle(5, 160)
    setheading(90)
    
    fd(10)
    setheading(90)
    circle(5, 180)
    fd(10)
    
    left(180)
    left(20)
    fd(10)
    circle(5, 170)
    fd(10)
    setheading(240)
    circle(50, 30)
    
    end_fill()
    myposition(130, 125)
    setheading(-20)
    fd(5)
    circle(-5, 160)
    fd(5)
    
    # Fingers
    myposition(166, 130)
    setheading(-90)
    fd(3)
    circle(-4, 180)
    fd(3)
    setheading(-90)
    fd(3)
    circle(-4, 180)
    fd(3)
    
    # Tail
    myposition(168, 134)
    fillcolor('#F6D02F')
    begin_fill()
    setheading(40)
    fd(200)
    setheading(-80)
    fd(150)
    setheading(210)
    fd(150)
    left(90)
    fd(100)
    right(95)
    fd(100)
    left(110)
    fd(70)
    right(110)
    fd(80)
    left(110)
    fd(30)
    right(110)
    fd(32)
    
    right(106)
    circle(100, 25)
    right(15)
    circle(-300, 2)
    #print(pos())
    setheading(30)
    fd(40)
    left(100)
    fd(70)
    right(100)
    fd(80)
    left(100)
    fd(46)
    setheading(66)
    circle(200, 38)
    right(10)
    fd(10)
    end_fill()
    
    # Tail Pattern
    fillcolor('#923E24')
    myposition(126.82, -156.84)
    begin_fill()
    
    setheading(30)
    fd(40)
    left(100)
    fd(40)
    pencolor('#923e24')
    setheading(-30)
    fd(30)
    left(140)
    fd(20)
    right(150)
    fd(20)
    left(150)
    fd(20)
    right(150)
    fd(20)
    left(130)
    fd(18)
    pencolor('#000000')
    setheading(-45)
    fd(67)
    right(110)
    fd(80)
    left(110)
    fd(30)
    right(110)
    fd(32)
    right(106)
    circle(100, 25)
    right(15)
    circle(-300, 2)
    end_fill()
    
    # Eye, Mouth, Cheek
    mouth(-5, 25)
    leftCheek(-126, 32)
    rightCheek(107, 63)
    colorLeftEar(-250, 100)
    colorRightEar(140, 270)
    leftEye(-85, 90)
    rightEye(50, 110)
    hideturtle()


body()
done()