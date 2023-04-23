def ex1():
    scores = [78, 56, 67, int(input('Input new score: '))]

    scores.sort(reverse=True)

    print('High scores:')
    for i, score in enumerate(scores):
        print(f'{i + 1}. {score}')


ex1()
