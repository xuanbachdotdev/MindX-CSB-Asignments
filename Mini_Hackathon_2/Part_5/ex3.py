def ex3():
    names = ["BĐ", "BTL", "CG", "ĐĐ", "HBT"]
    pops = [247100, 333300, 266800, 420900, 318000]

    min_pos = 0
    max_pos = 0
    for i, el in enumerate(pops[1:]):
        if el < pops[min_pos]:
            min_pos = i
        if el > pops[max_pos]:
            max_pos = i

    print("Names of:")
    print("- Most populated dist.:", names[max_pos])
    print("- Least populated dist.:", names[min_pos])


ex3()
