def ex3():
    scores = [78, 56, 67]

    scores.append(int(input('Input new score: ')))

    print('High scores:')
    for i, score in enumerate(scores):
        print(f'{i + 1}. {score}')


ex3()
