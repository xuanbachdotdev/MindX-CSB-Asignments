from turtle import *


def ex6():
    input_edge = int(input("Input number of edges:"))
    if input_edge <= 2:
        print("Invalid")
    if input_edge > 2:
        angle = ((input_edge - 2) * 180)/input_edge
        shape('turtle')
        for i in range(input_edge):
            forward(100)
            right(180 - angle)
        mainloop()


ex6()

