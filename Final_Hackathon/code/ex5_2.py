phones = {
    "Iphone12": 28000000,
    "Samsung N10": 16000000,
    "Oppo 93": 7500000,
    "Vsmart": 7400000,
    "Vivo": 4200000,
}

budget = int(input("Input your budget: "))

for item in phones.items():
    if item[1] <= budget:
        print("- %s: %d" % (item[0], item[1]))
