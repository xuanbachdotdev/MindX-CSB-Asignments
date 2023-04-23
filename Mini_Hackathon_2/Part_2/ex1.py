def ex1():
    colors = ['blue', 'teal', 'green']

    print('Color list:')
    for color in colors[:-1]:
        print(color, end=', ')
    print(colors[-1])

    position = int(input('Input position: '))

    print(f'Color at position {position}: {colors[position - 1]}')


ex1()
