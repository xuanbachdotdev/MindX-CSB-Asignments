def ex4():
    input_num = int(input("Input number: "))
    if input_num % 3 == 0:
        if input_num % 5 == 0:
            print(f"{input_num} is divisible by 3 and 5")
        else:
            print(f"{input_num} is divisible by 3")
    elif input_num % 5 == 0:
        if input_num % 3 == 0:
            print(f"{input_num} is divisible by 3 and 5")
        else:
            print(f"{input_num} is divisible by 5")
    else:
        print(f"{input_num} is not divisible by 3 or 5")


ex4()
