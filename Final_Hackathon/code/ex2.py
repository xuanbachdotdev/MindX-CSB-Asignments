a = float(input("Input a: "))
b = float(input("Input b: "))
c = float(input("Input c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("The equation has Infinite solutions.")
        else:
            print("The equation has no solution.")
    else:
        if c == 0:
            print("The equation has 1 solution.\n x = 0")
        else:
            print("The equation has 1 solution.\n x = ", -c / b)
else:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("The equation has no solution.")
    elif delta == 0:
        print("The equation has 1 solution.\n x = ", -b / (2 * a))
    else:
        print("The equation has 2 solutions.")
        print("x = ", float((-b - delta ** 1/2) / (2 * a)), end=" or ")
        print("x = ", float((-b + delta ** 1/2) / (2 * a)))