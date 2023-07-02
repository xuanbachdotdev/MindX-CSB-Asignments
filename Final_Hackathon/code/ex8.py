num = int(input('Input a number: '))

if num < 0:
    print("Please enter a positive number!")
else:
    print('First %d Fibonacci number(s): ' % num, end='')
    if num == 0 or num == 1:
        print(num)
    else:
        fibonacci = [1, 1]
        for i in range(2, num):
            fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
        for el in fibonacci:
            print(el, end=' ')

