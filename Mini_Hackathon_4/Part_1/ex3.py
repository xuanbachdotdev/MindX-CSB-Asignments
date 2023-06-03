number_of_computer_types = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30
}


inp_brand = input("Input a brand: ")

print(
    f"Available {inp_brand}s : {number_of_computer_types[inp_brand]}" if inp_brand in number_of_computer_types else "Not found")
