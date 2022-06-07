from turtle import *

bgcolor("black")
left(90)
speed(0)


def draw(len):
    if (len < 10):
        return
    else:
        pensize(2)
        pencolor("yellow")
        forward(len)
        left(30)
        draw(3 * len / 4)
        right(60)
        draw(3 * len / 4)
        left(30)
        pensize(2)
        backward(len)
        
        
draw(20)
right(90)


def draw(len):
    if (len < 10):
        return
    else:
        pensize(2)
        pencolor("magenta")
        forward(len)
        left(30)
        draw(3 * len / 4)
        right(60)
        draw(3 * len / 4)
        left(30)
        pensize(2)
        backward(len)


draw(20)
left(270)


def draw(len):
    if (len < 10):
        return
    else:
        pensize(2)
        pencolor("red")
        forward(len)
        left(30)
        draw(3 * len / 4)
        right(60)
        draw(3 * len / 4)
        left(30)
        pensize(2)
        backward(len)


draw(20)
right(90)


def draw(len):
    if (len < 10):
        return
    else:
        pensize(2)
        pencolor('#FFF8DC')
        forward(len)
        left(30)
        draw(3 * len / 4)
        right(60)
        draw(3 * len / 4)
        left(30)
        pensize(2)
        backward(len)


draw(20)


def draw(len):
    if (len < 10):
        return
    else:
        pensize(3)
        pencolor("lightgreen")
        forward(len)
        left(30)
        draw(4 * len / 5)
        right(60)
        draw(4 * len / 5)
        left(30)
        pensize(3)
        backward(len)


draw(40)
right(90)


def draw(len):
    if (len < 10):
        return
    else:
        pensize(3)
        pencolor("red")
        forward(len)
        left(30)
        draw(4 * len / 5)
        right(60)
        draw(4 * len / 5)
        left(30)
        pensize(3)
        backward(len)


draw(40)
left(270)


def draw(len):
    if (len < 10):
        return
    else:
        pensize(3)
        pencolor("yellow")
        forward(len)
        left(30)
        draw(4 * len / 5)
        right(60)
        draw(4 * len / 5)
        left(30)
        pensize(3)
        backward(len)


draw(40)
right(90)


def draw(len):
    if (len < 10):
        return
    else:
        pensize(3)
        pencolor('#FFF8DC')
        forward(len)
        left(30)
        draw(4 * len / 5)
        right(60)
        draw(4 * len / 5)
        left(30)
        pensize(3)
        backward(len)


draw(40)


def draw(len):
    if (len < 10):
        return
    else:
        pensize(2)
        pencolor("cyan")
        forward(len)
        left(30)
        draw(6 * len / 7)
        right(60)
        draw(6 * len / 7)
        left(30)
        pensize(2)
        backward(len)


draw(60)
right(90)


def draw(len):
    if (len < 10):
        return
    else:
        pensize(2)
        pencolor("yellow")
        forward(len)
        left(30)
        draw(6 * len / 7)
        right(60)
        draw(6 * len / 7)
        left(30)
        pensize(2)
        backward(len)


draw(60)
left(270)


def draw(len):
    if (len < 10):
        return
    else:
        pensize(2)
        pencolor("magenta")
        forward(len)
        left(30)
        draw(6 * len / 7)
        right(60)
        draw(6 * len / 7)
        left(30)
        pensize(2)
        backward(len)


draw(60)
right(90)


def draw(len):
    if (len < 10):
        return
    else:
        pensize(2)
        pencolor('#FFF8DC')
        forward(len)
        left(30)
        draw(6 * len / 7)
        right(60)
        draw(6 * len / 7)
        left(30)
        pensize(2)
        backward(len)


draw(60)

done()
