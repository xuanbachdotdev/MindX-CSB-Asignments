def ex3():
    print('== Registration ==')
    input('Username: ')
    while True:
        password = input('Password: ')
        is_has_letter = False
        is_has_digits = False
        for ch in password:
            if ('a' < ch < 'z') or ('A' < ch < 'Z'):
                is_has_letter = True
            if '0' < ch < '9':
                is_has_digits = True

        if is_has_letter and is_has_digits and len(password) >= 8:
            break
        else:
            print('Invalid password. Please input again.')
    while True:
        if input('Repeat password: ') == password:
            break
        else:
            print('Passwords not match. Please input again.')
    while True:
        email = input('Email: ')
        if ('.' in email) and ('@' in email):
            break
        else:
            print('Invalid email. Please input again.')
    print('Registered successfully.')


ex3()
