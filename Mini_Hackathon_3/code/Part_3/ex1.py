import random
import msvcrt
import os

MAP_COLlUMS = 10
MAP_ROWS = 8


def gen_obj(map, obj_char):
    while True:
        rand_row_pos = random.randint(0, MAP_ROWS - 1)
        rand_col_pos = random.randint(0, MAP_COLlUMS - 1)
        if map[rand_row_pos][rand_col_pos] == "-":
            map[rand_row_pos][rand_col_pos] = obj_char
            break


def make_map():
    map = [["-" for i in range(MAP_COLlUMS)] for i in range(MAP_ROWS)]
    map[0][0] = "P"
    gen_obj(map, "K")
    gen_obj(map, "D")
    return map


def print_map(map):
    for r in range(MAP_ROWS):
        for c in range(MAP_COLlUMS):
            print(map[r][c], end=' ')
        print()


def move(map, ch, r_P, c_P):
    r_P_new = r_P
    c_P_new = c_P
    if ch == 'W':
        r_P_new = max(0, r_P - 1)
    elif ch == 'S':
        r_P_new = min(MAP_ROWS - 1, r_P + 1)
    elif ch == 'A':
        c_P_new = max(0, c_P - 1)
    elif ch == 'D':
        c_P_new = min(MAP_COLlUMS - 1, c_P + 1)
    value = map[r_P_new][c_P_new]
    map[r_P][c_P] = '-'
    map[r_P_new][c_P_new] = 'P'
    return r_P_new, c_P_new, value


def main():
    map = make_map()
    r_P = 0
    c_P = 0
    found_key = False
    os.system('cls')
    print_map(map)
    print('\n== THE ESCAPE GAME ==')
    print('Use W A S D to move (P)layer.')
    print('Find (K)ey first then exit through the (D)oor.')
    while True:
        ch = msvcrt.getch().decode('utf-8').upper()
        r_P, c_P, value = move(map, ch, r_P, c_P)
        if value == 'K':
            found_key = True
        elif value == 'D':
            os.system('cls')
            print_map(map)
            if found_key:
                print('YOU WON!!!')
            else:
                print('YOU LOSE.')
                print('Maybe find the Key first?')
            break
        os.system('cls')
        print_map(map)


main()
