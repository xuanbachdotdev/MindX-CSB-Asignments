inp = float(input("Input number: "))


def is_int(num: float) -> bool:
    return num.is_integer()


if is_int(inp):
    print(f'{int(inp)} is an integer')
else:
    print(f'{inp} is not an integer')
