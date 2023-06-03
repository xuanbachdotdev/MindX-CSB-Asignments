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

print("Total value of available brands:")
for el in number_of_computer_types.items():
    print('-',el[0], ":", number_of_computer_types[el[0]]*price_of_computer_types[el[0]])
    