def ex3():
    input_num = int(input("Input number: "))
    factorial = 1
    if input_num < 0:
        print("Invalid")
    elif input_num == 0 or input_num == 1:
        print(factorial)
    else:
        for i in range(2, input_num + 1):
            factorial *= i
        print(f"{input_num}! = {factorial}")


ex3()
