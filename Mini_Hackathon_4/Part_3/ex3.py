price_of_computer_types = {
    "HP": 600,
    "DELL": 650,
    "MACBOOK": 1200,
    "ASUS": 400
}

inp = input("Input a brand: ")

print(("Price of %s: %d" % (inp,
      price_of_computer_types[inp])) if inp in price_of_computer_types else "Not found")
