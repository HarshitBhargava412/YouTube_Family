from turtle import *

bgcolor("black")
color("#ffde40")
hideturtle()
speed(6)


def pubg():
    penup()
    goto(0, 100)
    pendown()


def pubg_block():
    pensize(9)
    forward(170)
    left(45)
    forward(6)
    left(45)
    forward(170)
    left(45)
    forward(6)
    left(45)
    forward(330)
    left(45)
    forward(6)
    left(45)
    forward(170)
    left(45)
    forward(6)
    left(45)
    forward(170)
    
    
def lines():
    pensize(12)
    penup()
    forward(180)
    left(90)
    forward(35)
    left(90)
    pendown()
    forward(12)
    
    penup()
    forward(344)
    pendown()
    forward(17)
    
    penup()
    right(90)
    forward(105)
    right(90)
    pendown()
    forward(17)
    
    penup()
    forward(344)
    pendown()
    forward(12)
    
    
def letter_pubg_p():
    penup()
    left(180)
    forward(280)
    pendown()
    forward(40)
    left(90)
    forward(100)
    left(180)
    forward(52)
    right(90)
    forward(40)
    left(90)
    forward(47)
    
    
def letter_pubg_u():
    penup()
    right(90)
    forward(32)
    right(90)
    pendown()
    forward(98)
    left(90)
    forward(40)
    left(90)
    forward(98)
    
    
def letter_pubg_b():
    penup()
    right(90)
    forward(35)
    pendown()
    forward(45)
    right(90)
    forward(40)
    right(45)
    forward(8)
    right(45)
    forward(35)
    left(90)
    forward(8)
    left(90)
    forward(35)
    right(45)
    forward(8)
    right(45)
    forward(40)
    right(90)
    forward(45)
    right(90)
    forward(100)
    
    
def letter_pubg_g():
    penup()
    right(180)
    forward(53)
    left(90)
    forward(98)
    pendown()
    forward(25)
    right(90)
    forward(45)
    right(90)
    forward(45)
    right(90)
    forward(95)
    right(90)
    forward(45)


def bgmi():
    penup()
    goto(0, -200)
    pendown()


def bgmi_block():
    color("#498c0d")
    pensize(9)
    forward(170)
    left(45)
    forward(6)
    left(45)
    forward(85)
    color("#ee8027")
    forward(85)
    left(45)
    forward(6)
    left(45)
    forward(330)
    left(45)
    forward(6)
    left(45)
    forward(85)
    color("#498c0d")
    forward(85)
    left(45)
    forward(6)
    left(45)
    forward(170)


def letter_bgmi_b():
    color("white")
    pensize(14)
    penup()
    backward(135)
    left(90)
    forward(140)
    right(90)
    pendown()
    forward(45)
    right(90)
    forward(40)
    right(45)
    forward(8)
    right(45)
    forward(35)
    left(90)
    forward(8)
    left(90)
    forward(35)
    right(45)
    forward(8)
    right(45)
    forward(40)
    right(90)
    forward(45)
    right(90)
    forward(100)


def letter_bgmi_g():
    color("white")
    pensize(14)
    penup()
    right(180)
    forward(53)
    left(90)
    forward(103)
    pendown()
    forward(25)
    right(90)
    forward(45)
    right(90)
    forward(45)
    right(90)
    forward(95)
    right(90)
    forward(45)


def letter_bgmi_m():
    color("white")
    pensize(14)
    penup()
    forward(40)
    right(90)
    forward(95)
    left(180)
    pendown()
    forward(96)
    right(150)
    forward(55)
    left(120)
    forward(55)
    setheading(0)
    right(90)
    forward(96)


def letter_bgmi_i():
    color("white")
    pensize(14)
    penup()
    left(90)
    forward(40)
    left(90)
    pendown()
    forward(96)
    
    
pubg()
pubg_block()
lines()
letter_pubg_p()
letter_pubg_u()
letter_pubg_b()
letter_pubg_g()

bgmi()
bgmi_block()
letter_bgmi_b()
letter_bgmi_g()
letter_bgmi_m()
letter_bgmi_i()

done()