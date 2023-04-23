def ex2():
    print('Input the list of numbers.')
    print('Enter 0 to finish')

    arr = []
    while True:
        num = int(input())
        if num == 0:
            break
        if num % 2 == 0:
            arr.append(num)

    print('Even numbers in list: ', end='')
    for el in arr:
        print(el, end=' ')


ex2()
