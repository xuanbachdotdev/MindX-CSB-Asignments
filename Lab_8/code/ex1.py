inp = float(input("Input number: "))


def is_int(num: float) -> bool:
    return True if num % 1 == 0 else False


if is_int(inp):
    print('%d is an integer' % inp)
else:
    print('%d is not an integer' % inp)
