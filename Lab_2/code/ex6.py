from turtle import *


def ex6():
    shape('turtle')
    for i in range(2):
        pensize(2)
        pencolor('#000')
        forward(100)
        right(90)
        pensize(6)
        pencolor('#de5246')
        forward(80)
        right(90)

    right(45)
    forward(70)
    left(90)
    forward(70)

    mainloop()


ex6()