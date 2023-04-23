from turtle import *


def ex3():
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']

    shape('turtle')
    pensize(3)
    for color in colors:
        pencolor(color)
        forward(30)
        penup()
        forward(20)
        pendown()

    mainloop()


ex3()
