price_of_computer_types = {
    "HP": 600,
    "DELL": 650,
    "MACBOOK": 1200,
    "ASUS": 400,
}

inp_brand = input("Input a brand: ")

print(("Total price: %s" % (price_of_computer_types[inp_brand]*int(input(
    "Input amount to buy: ")))) if inp_brand in price_of_computer_types else "Not found")
