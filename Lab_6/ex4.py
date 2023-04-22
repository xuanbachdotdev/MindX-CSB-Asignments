def ex4():
    num = int(input('Number of items: '))

    arr = []
    for i in range(num):
        print(f'\nItem {i + 1}: ', end='')
        name = input()
        print(f'Price of item {i + 1}: ', end='')
        price = float(input())
        arr.append((name, price))

    total = 0
    for item in arr:
        total += item[1]
    avg = total / num
    print('Average price:', avg)

    print('Item(s) above average price: ', end='')
    for item in arr:
        if item[1] > avg:
            print(item, end=' ')


ex4()
