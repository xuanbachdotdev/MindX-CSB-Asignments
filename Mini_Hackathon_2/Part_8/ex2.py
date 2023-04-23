def ex2():
    scores = [78, 70, 67, 56, 45, int(input('Input new score: '))]

    scores.sort(reverse=True)

    scores = scores[:5]

    print('High scores:')
    for i, score in enumerate(scores):
        print(f'{i + 1}. {score}')


ex2()
