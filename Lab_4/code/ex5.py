def ex5():
    print("Number with sum of digits = 9:")
    i = 1000
    temp = 1
    while i >= 1000 and temp < 11:
        i += 1
        sum = 0
        for digit in str(i):
            sum += int(digit)
        if sum == 9:
            temp += 1
            print(i, end=" ")


ex5()

