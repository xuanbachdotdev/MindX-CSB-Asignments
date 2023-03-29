def ex2():
    first_name = input("First name: ") + " "
    last_name = input("Last name: ")
    phone_number = input("Phone number: ")

    if type(phone_number) == int:
        print(f"Your registered name is {first_name + last_name}")
        print(f"Your phone number is {phone_number}")
    else:
        print("Please enter the correct phone number!")


ex2()
