def division_of_factorial(num: int) -> int:
    temp = 1
    for i in range(2, num):
        temp *= i
    return temp


total = 0

for i in range(1, int(input("Input number: ")) + 1):
    total += division_of_factorial(i)
print("Result: %d" % total)
