def ex3(num: int) -> int:
    factorial = 1
    for i in range(2, num):
        factorial *= i
    return factorial


total = 0

for i in range(1, int(input("Input number: ")) + 1):
    total += ex3(i)
print("Result: %d" % total)
