def ex2():
    print('== Registration ==')
    input('Username: ')
    password = input('Password: ', )
    while True:
        print('Repeat password: ', end='')
        if input() == password:
            break
        else:
            print('Passwords not match. Please input again.')
    input('Email: ')
    print('Registered successfully.')


ex2()

