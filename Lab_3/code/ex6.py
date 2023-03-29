def ex6():
    a = input("Input length 1: ")
    b = input("Input length 2: ")
    c = input("Input length 3: ")
    if a + b <= c or a + c <= b or b + c <= a:
        print("The 3 line segments can form a triangle.")
    else:
        print("The 3 line segments cannot form a triangle.")


ex6()
