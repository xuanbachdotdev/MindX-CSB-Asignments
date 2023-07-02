phones = {
    "Iphone12": 28000000,
    "Samsung N10": 16000000,
    "Oppo 93": 7500000,
    "Vsmart": 7400000,
    "Vivo": 4200000,
}

inp_phone_name = input("Input name of a phone: ")
if inp_phone_name in phones:
    print("Price of %s: %d" % (inp_phone_name, phones[inp_phone_name]))
else:
    print("Please enter the correct phone name")
