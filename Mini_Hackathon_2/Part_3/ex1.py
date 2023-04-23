def ex1():
    arr = [5, 1, 8, 92, -1, 30]

    num = int(input('Input a number: '))

    pos = None
    for i, el in enumerate(arr):
        if el == num:
            pos = i + 1
            break

    if pos is None:
        print('Number not found')
    else:
        print(f'Number found at position {pos}')


ex1()
