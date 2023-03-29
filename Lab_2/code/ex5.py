def ex5():
    deposit = float(input("Deposit: "))
    years = [1, 2, 10]
    for i in years:
        print(f"Account after {i} year: {deposit*(105**i)}")


ex5()
