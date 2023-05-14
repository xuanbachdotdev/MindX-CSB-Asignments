def is_palindrome(string: str) -> bool:
    return True if string[::-1] == string else False


print("This is a palindrome." if is_palindrome(input("Input a text: ")) else "This is not a palindrome.")
