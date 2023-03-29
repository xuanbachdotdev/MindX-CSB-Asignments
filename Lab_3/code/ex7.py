from turtle import *


def ex7():
    a = int(input("Input length 1: "))
    b = int(input("Input length 2: "))
    c = int(input("Input length 3: "))
    if a + b <= c or a + c <= b or b + c <= a:
        print("The 3 line segments cannot form a triangle.")
    else:
        if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == b**2 + a**2:
            print("The 3 line segments can form a right triangle.")
        elif a == b == c:
            print("The 3 line segments can form an equilateral triangle.")
            shape('turtle')
            forward(a)
            left(120)

            forward(b)
            left(120)

            forward(c)

            mainloop()
        else:
            print("The 3 line segments can form a triangle.")


ex7()
