import re


def ex4():
    date_regex = "^[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}$"

    date_input = input("Date in MM/DD/YYYY format: ")
    if re.match(date_regex, date_input):
        temp = date_input.split("/")
        print(f"Date in DD/MM/YYYY format: {temp[1]}/{temp[0]}/{temp[2]}")
    else:
        print("Please enter correct type of date!")


ex4()
