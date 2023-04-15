from turtle import *


def ex4():
    edges = int(input("Input number of edges: "))

    if edges <= 2: print("Please enter the correct number of edges")

    angle = (edges - 2) * 180 / edges
    shape('turtle')
    for i in range(edges):
        forward(100)
        right(180 - angle)

    mainloop()


ex4()
