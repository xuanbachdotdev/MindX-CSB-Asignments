def is_palindrome(string: str) -> bool:
    return string[::-1] == string

print("This is a palindrome." if is_palindrome(input("Input a text: ")) else "This is not a palindrome.")