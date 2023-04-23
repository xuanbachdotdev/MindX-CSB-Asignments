def ex2():
    colors = ['blue', 'teal', 'green']

    print('Color list:')
    for color in colors[:-1]:
        print(color, end=', ')
    print(colors[-1])

    inp = input('Item to delete: ')

    if "0" <= inp <= f"{len(colors)}":
        colors.pop(int(inp) - 1)
    else:
        colors.remove(inp)

    print('New color list:')
    for color in colors[:-1]:
        print(color, end=', ')
    print(colors[-1])


ex2()
