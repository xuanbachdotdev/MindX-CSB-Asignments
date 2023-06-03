number_of_computer_types = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30
}

price_of_computer_types = {
    "HP": 600,
    "DELL": 650,
    "MACBOOK": 1200,
    "ASUS": 400,
}

inp_brand = input("Input a brand: ")

if inp_brand in price_of_computer_types:
    inp_val = int(input(
        "Input amount to buy: "))
    print(("Total price: %s" % (price_of_computer_types[inp_brand]*inp_val)))
    number_of_computer_types[inp_brand] -= inp_val
    print("Available products:")
    for el in number_of_computer_types.items():
        print("-", el[1], el[0])
else:
    print("Not found")
