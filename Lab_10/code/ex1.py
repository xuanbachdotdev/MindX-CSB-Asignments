numbers = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5,
           'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10}
inp = input("Input a Roman number: ")
print(f"Arabic number: {numbers[inp]}" if inp in numbers else "Not found")