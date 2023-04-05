def ex4():
    input_num = int(input("Input number: "))
    sum = 0
    for digit in str(input_num):
        sum += int(digit)
    print(f"Sum of digits of {input_num}: {sum}")


ex4()
