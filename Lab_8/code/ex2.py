def is_prime(x: int) -> bool:
    divided_by = 0

    if x <= 0:
        return False
    if x == 1:
        return False
    if x == 2:
        return True

    for n in range(2, x):
        if x % n == 0:
            divided_by += 1

    if divided_by != 0:
        return False
    else:
        return True


num = int(input("Input number: "))
print("%d is a prime" % num if is_prime(num) else "%d is not a prime" % num)
