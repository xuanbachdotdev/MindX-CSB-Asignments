def ex5():
    input_str = input(str('Write a sentence: '))
    word_list = input_str.split(' ')

    unique_word_list = []
    for word in word_list:
        if not (word in unique_word_list):
            unique_word_list.append(word)

    print('Number of unique words:', len(unique_word_list))


ex5()
