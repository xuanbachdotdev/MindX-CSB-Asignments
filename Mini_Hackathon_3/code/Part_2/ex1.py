import sys


def factorial(num: int) -> int:
    total = 1
    if num < 0:
        print("Invalid")
        sys.exit()
    elif num == 0 or num == 1:
        return total
    else:
        for i in range(2, num + 1):
            total *= i
        return total


num = int(input("Input a number: "))
print("%d! = %d" % (num, factorial(num)))
