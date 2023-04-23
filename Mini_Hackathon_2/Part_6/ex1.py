def ex1():
    names = ['BĐ', 'BTL', 'CG', 'ĐĐ', 'HBT']
    areas = [9.224, 43.35, 12.04, 9.96, 10.09]
    populations = [247100, 333300, 266800, 420900, 318000]

    density = []
    for i in range(len(areas)):
        density.append(populations[i] / areas[i])

    print('Population density of:')
    for i in range(len(areas)):
        print(f'- {names[i]}: {density[i]}')


ex1()
