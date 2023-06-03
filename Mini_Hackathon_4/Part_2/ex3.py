number_of_computer_types = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30
}

number_of_computer_types["DELL"] = 60
number_of_computer_types["MACBOOK"] = 2


print("Available products:")
for key in number_of_computer_types:
    print(f"- {key}: {number_of_computer_types[key]}")