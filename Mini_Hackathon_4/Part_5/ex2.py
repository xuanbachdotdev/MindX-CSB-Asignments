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

sum = 0

for el in number_of_computer_types.items():
    sum += number_of_computer_types[el[0]]*price_of_computer_types[el[0]]
    
print("Total value of available items:", sum)
    