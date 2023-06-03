number_of_computer_types = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30
}

sum = 0

for val in number_of_computer_types.values():
    sum += val

print("Total products: %d" % sum)