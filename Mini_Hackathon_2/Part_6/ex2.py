def ex2():
    areas = [9.224, 43.35, 12.04, 9.96, 10.09]
    populations = [247100, 333300, 266800, 420900, 318000]

    density = []
    for i in range(len(areas)):
        density.append(populations[i] / areas[i])

    print('Average population density:', sum(density) / len(density))


ex2()
