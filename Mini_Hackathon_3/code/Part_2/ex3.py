def print_fibo(num: int):
    if num < 0:
        return -1
    if num == 0 or num == 1:
        return num
    fibonacci = [1, 1]
    for i in range(2, num):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    for el in fibonacci:
        print(el, end=' ')


num = int(input('Input a number: '))
print('First %d Fibonacci number(s): ' % num, end='')
print_fibo(num)
