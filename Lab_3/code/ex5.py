def ex5():
    print("Welcome to The Ultimate Security System")
    username = input("Username: ")
    password = input("Password: ")
    if username == "admin" and password == "12345":
        print(f"You are logged in, {username}.")
    else:
        print("Wrong username or password.")


ex5()
