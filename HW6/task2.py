import random

PLACEMENTS = 4


def solve_chess_puzzle(queens: list):
    ys, xs, d1, d2 = set(), set(), set(), set()
    q_counter = 0
    for y, row in enumerate(queens):
        for x, ch in enumerate(row):
            if ch == 'Q':
                q_counter += 1
                ys.add(y)
                xs.add(x)
                d1.add(y + x)
                d2.add(y - x)
                if not (q_counter == len(ys) == len(xs) == len(d1) == len(d2)):
                    return False
    return True


def random_check(chess_size: int = 8):
    counter = 0
    while counter < PLACEMENTS:
        chess_board = [[' ' for _ in range(chess_size)] for _ in range(chess_size)]
        set_num = [_ for _ in range(chess_size)]
        for j in range(chess_size):
            random.shuffle(set_num)
            i = set_num.pop()
            chess_board[j][i] = 'Q'
        chess_board_ = [''.join(row) for row in chess_board]
        if solve_chess_puzzle(chess_board_):
            print(f'\t\t\tSolution: {counter+1}')
            for rows in chess_board:
                print(f'{rows}')
            counter += 1
            print(f'----------------------------------------')


if __name__ == '__main__':
    # solution for task 2
    queens_true = [
        ' Q  ',
        '   Q',
        'Q   ',
        '  Q '
    ]

    print(solve_chess_puzzle(queens_true))

    # solution for task 3
    random_check()

