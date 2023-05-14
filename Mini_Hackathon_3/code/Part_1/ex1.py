def is_even(num: int) -> bool:
    return True if num % 2 == 0 else False


print("This number is even" if is_even(int(input("Input a number: "))) else "This number is not even")
