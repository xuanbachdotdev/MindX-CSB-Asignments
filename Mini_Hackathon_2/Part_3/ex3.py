def ex3():
    print('Input the list of numbers.')
    print('Enter 0 to finish')

    sum = 0
    while True:
        num = int(input())
        if num == 0:
            break
        sum += num

    print('Sum of numbers in list:', sum)


ex3()
