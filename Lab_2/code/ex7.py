from turtle import *


def ex7():
    shape('turtle')
    right(30)
    pensize(10)
    for i in range(2):
        pencolor('#cf8f03')
        forward(100)
        right(120)
        forward(100)
        right(60)

    left(30)
    penup()
    forward(40)
    right(30)
    pendown()

    for i in range(2):
        pencolor('#0b2c3c')
        forward(100)
        right(120)
        forward(100)
        right(60)

    mainloop()


ex7()
