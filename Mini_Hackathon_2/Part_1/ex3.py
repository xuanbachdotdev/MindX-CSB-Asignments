def ex3():
    colors = ['blue', 'teal', 'green']

    print('Color list:')
    for color in colors[:-1]:
        print(color, end=', ')
    print(colors[-1])

    color = input('Input a new color: ')
    colors.append(color)

    print('New color list:')
    for color in colors[:-1]:
        print(color, end=', ')
    print(colors[-1])


ex3()
