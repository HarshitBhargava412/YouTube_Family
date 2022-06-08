from turtle import *

bgcolor('black')
color('white')
rotate = int(180)
speed(0)
setup(1920, 1080, 0, 0)


def circles(size):
    for i in range(10):
        circle(size)
        size = size - 4


def repeats1():
    for i in range (10):
        circles(200)
        right(360/10)
    
        
repeats1()
color('yellow')
rotate = int(90)


def circles(size):
    for i in range(4):
        circle(size)
        size = size-10


def repeats1():
    for i in range(10):
        circles(160)
        right(360/10)


repeats1()
color('blue')
rotate = int(80)


def circles(size):
    for i in range(4):
        circle(size)
        size = size-5


def repeats1():
    for i in range(10):
        circles(120)
        right(360/10)


repeats1()
color('red')
rotate = int(90)


def circles(size):
    for i in range(4):
        circle(size)
        size = size-19


def repeats1():
    for i in range (10):
        circles(80)
        right(360/10)


repeats1()
color('green')
rotate = int(90)


def circles(size):
    for i in range(4):
        circle(size)
        size = size-20


def repeats1():
    for i in range (10):
        circles(40)
        right(360/10)


repeats1()

done()