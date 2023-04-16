import random


def ex1():
    print('== FREAKING MATH CONSOLE ==')
    print('Give correct answers to get scores.')
    score = 0
    while True:
        op = random.randint(0, 3)
        left_operand = None
        right_operand = None
        result = None
        operand_char = None
        if op == 0:
            operand_char = '+'
            left_operand = random.randint(0, 30)
            right_operand = random.randint(0, 30)
            result = left_operand + right_operand

        elif op == 1:
            operand_char = '-'
            left_operand = random.randint(0, 30)
            right_operand = random.randint(0, 30)
            result = left_operand - right_operand

        elif op == 2:
            operand_char = '*'
            left_operand = random.randint(0, 10)
            right_operand = random.randint(0, 10)
            result = left_operand * right_operand

        elif op == 3:
            operand_char = '/'
            right_operand = random.randint(0, 10)
            result = random.randint(0, 10)
            left_operand = right_operand * result

        correct = random.randint(0, 1)
        if not correct:
            result += (random.randint(1,10) - 10 + 1) * random.randint(1, 5)

        print(f'{left_operand} {operand_char} {right_operand} = {result}')
        print('1 for True, 0 for False: ', end="")
        if str(correct) == input():
            score += 1
            print(f'Score: {score}\n')
        else:
            print('Incorrect.\n')
            break

    print('== GAME OVER ==')
    print(f'Your total score is {score}')


ex1()
