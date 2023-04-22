def ex1(original_list: list):
    add_2 = [el + 2 for el in original_list]
    multiply_by_2 = [el * 2 for el in original_list]
    shift_2 = original_list[2:] + original_list[:2]
    print(f"Original list : {original_list}\n")
    print(f'Add 2         : {add_2}')
    print(f'Multiply by 2 : {multiply_by_2}')
    print(f'Shift 2       : {shift_2}')


ex1(list(range(10)))
