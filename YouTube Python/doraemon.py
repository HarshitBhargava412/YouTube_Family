from turtle import *

speed(20)
pensize(3)


def myposition(x, y):
    penup()
    goto(x, y)
    pendown()


def head():
    myposition(98, 35)
    left(40)
    fillcolor('#00a0de')
    begin_fill()
    circle(150, 280)
    end_fill()


def scarf():
    fillcolor('#e70010')
    begin_fill()
    setheading(0)
    forward(200)
    circle(-5, 90)
    forward(10)
    circle(-5, 90)
    forward(207)
    circle(-5, 90)
    forward(10)
    circle(-5, 90)
    end_fill()


def face():
    forward(183)
    left(45)
    fillcolor('#ffffff')
    begin_fill()
    circle(120, 100)
    setheading(180)
    forward(121)
    setheading(215)
    circle(120, 100)
    end_fill()
    myposition(63.56, 218.24)
    setheading(90)
    eyes()
    setheading(180)
    penup()
    forward(60)
    myposition(3.06, 218.24)
    setheading(90)
    eyes()
    penup()
    setheading(180)
    forward(64)


def eyes():
    fillcolor("#ffffff")
    begin_fill()
    forward(10)
    circle(30, 180)
    forward(18)
    circle(30.25, 180)
    forward(8)
    end_fill()


def black_eyes():
    setheading(0)
    myposition(-20, 195)
    fillcolor('#000000')
    begin_fill()
    circle(13)
    end_fill()
    
    myposition(25, 195)
    setheading(0)
    begin_fill()
    circle(13)
    end_fill()
    
    myposition(-17, 200)
    setheading(0)
    fillcolor('#ffffff')
    begin_fill()
    circle(5)
    end_fill()
    myposition(0, 0)
    
    myposition(23, 200)
    setheading(0)
    fillcolor('#ffffff')
    begin_fill()
    circle(5)
    end_fill()
    myposition(0, 0)


def nose():
    myposition(-10, 158)
    setheading(315)
    fillcolor('#e70010')
    begin_fill()
    circle(20)
    end_fill()


def mouth():
    myposition(5, 148)
    setheading(270)
    forward(100)
    setheading(0)
    circle(120, 50)
    setheading(230)
    circle(-120, 100)


def beard():
    myposition(-32, 135)
    setheading(165)
    forward(60)
    
    myposition(-32, 125)
    setheading(180)
    forward(60)
    
    myposition(-32, 115)
    setheading(193)
    forward(60)
    
    myposition(37, 135)
    setheading(15)
    forward(60)
    
    myposition(37, 125)
    setheading(0)
    forward(60)
    
    myposition(37, 115)
    setheading(-13)
    forward(60)


def body():
    myposition(0, 0)
    setheading(0)
    penup()
    circle(150, 50)
    pendown()
    setheading(30)
    forward(40)
    setheading(70)
    circle(-30, 270)
    
    fillcolor('#00a0de')
    begin_fill()
    setheading(230)
    forward(80)
    setheading(90)
    circle(1000, 1)
    setheading(-89)
    circle(-1000, 10)
    setheading(180)
    forward(70)
    setheading(90)
    circle(30, 180)
    setheading(180)
    forward(70)
    setheading(100)
    circle(-1000, 9)
    setheading(-86)
    circle(1000, 2)
    setheading(230)
    forward(40)
    circle(-30, 230)
    setheading(45)
    forward(81)
    setheading(0)
    forward(203)
    circle(5, 90)
    forward(10)
    circle(5, 90)
    forward(7)
    setheading(40)
    circle(150, 10)
    setheading(30)
    forward(40)
    end_fill()


def hands():
    setheading(70)
    fillcolor('#ffffff')
    begin_fill()
    circle(-30)
    end_fill()
    
    myposition(-133.97, -91.81)
    setheading(50)
    fillcolor('#ffffff')
    begin_fill()
    circle(30)
    end_fill()


def legs():
    myposition(103.74, -182.59)
    setheading(0)
    fillcolor('#ffffff')
    begin_fill()
    forward(15)
    circle(-15, 180)
    forward(90)
    circle(-15, 180)
    forward(10)
    end_fill()
    
    myposition(-96.26, -182.59)
    setheading(180)
    fillcolor('#ffffff')
    begin_fill()
    forward(15)
    circle(15, 180)
    forward(90)
    circle(15, 180)
    forward(10)
    end_fill()


def stomach():
    myposition(-103.42, 15.09)
    setheading(0)
    forward(38)
    setheading(230)
    begin_fill()
    circle(90, 260)
    end_fill()


def pocket():
    myposition(5, -40)
    setheading(0)
    forward(70)
    setheading(-90)
    circle(-70, 180)
    setheading(0)
    forward(70)


def bell():
    myposition(-103.42, 15.09)
    forward(90)
    setheading(70)
    fillcolor('#ffd200')
    begin_fill()
    circle(-20)
    end_fill()
    
    setheading(170)
    fillcolor('#ffd200')
    begin_fill()
    circle(-2, 180)
    setheading(10)
    circle(-100, 22)
    circle(-2, 180)
    setheading(180 - 10)
    circle(100, 22)
    end_fill()
    goto(-13.42, 15.09)
    setheading(250)
    circle(20, 110)
    setheading(90)
    forward(15)
    dot(10)


head()
scarf()
face()
black_eyes()
nose()
mouth()
beard()
body()
hands()
legs()
stomach()
pocket()
bell()

hideturtle()

done()