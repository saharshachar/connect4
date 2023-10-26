import numpy as np

# constants
NUM_ROWS = 6  # number of rows
NUM_COLMS = 7  # number of columns
NUM_OF_PLAYERS = 2  # number of players
# values in cells for player each player (must not be non negative and in the length of NUM_OF_PLAYERS)
PLAYER_MARKS = [0, 3]
# value of an empty cell
EMPTY_CELL_VALUE = -1
WINNING_STRIKE = 4  # number of pieces in row for winning


def creat_board():
    board = np.ones([NUM_ROWS, NUM_COLMS]) * EMPTY_CELL_VALUE
    return board


def play_turn(board):
    valid_flag = False
    while not valid_flag:
        col_num = int(input())
        valid_flag = is_valid_turn(board, col_num)
        if not valid_flag:
            print("invalid input, try again")
        else:
            row_num = get_row_location_for_input(board, col_num)
            return row_num, col_num


def is_valid_turn(board, col_num):
    return board[0, col_num] == EMPTY_CELL_VALUE


def get_row_location_for_input(board, col_num):
    for curr_row_index in np.flip(range(NUM_ROWS)):
        if board[curr_row_index, col_num] == EMPTY_CELL_VALUE:
            return curr_row_index


def is_game_over(board):
    for curr_row in range(NUM_ROWS):
        for curr_col in range(NUM_COLMS):
            down_combo = check_down_combo(board, curr_row, curr_col, board[curr_row, curr_col])
            right_combo = check_right_combo(board, curr_row, curr_col, board[curr_row, curr_col])
            r_daig_combo = check_diag_combo(board, curr_row, curr_col, board[curr_row, curr_col], "right")
            l_daig_combo = check_diag_combo(board, curr_row, curr_col, board[curr_row, curr_col], "left")
            if down_combo in PLAYER_MARKS:
                return PLAYER_MARKS.index(down_combo)
            elif right_combo in PLAYER_MARKS:
                return PLAYER_MARKS.index(right_combo)
            elif r_daig_combo in PLAYER_MARKS:
                return PLAYER_MARKS.index(r_daig_combo)
            elif l_daig_combo in PLAYER_MARKS:
                return PLAYER_MARKS.index(l_daig_combo)
    return EMPTY_CELL_VALUE


def check_down_combo(board, initial_row, initial_col, curr_player_mark):
    if not (NUM_ROWS - initial_row >= WINNING_STRIKE):
        return EMPTY_CELL_VALUE  # no successful down combo
    else:
        for curr_row in range(initial_row, (initial_row + WINNING_STRIKE)):
            if board[curr_row, initial_col] != curr_player_mark:
                return EMPTY_CELL_VALUE  # no successful down combo
        return curr_player_mark  # current player has a successful down combo


def check_right_combo(board, initial_row, initial_col, curr_player_mark):
    if not (NUM_COLMS - initial_col >= WINNING_STRIKE):
        return EMPTY_CELL_VALUE  # no successful right combo
    else:
        for curr_col in range(initial_col, (initial_col + WINNING_STRIKE)):
            if board[initial_row, curr_col] != curr_player_mark:
                return EMPTY_CELL_VALUE  # no successful right combo
        return curr_player_mark  # current player has a successful right combo


def check_diag_combo(board, initial_row, initial_col, curr_player_mark, right_or_left_diag):
    if right_or_left_diag == "right":                             # right diagonal check
        initial_condi = NUM_COLMS - initial_col >= WINNING_STRIKE
        range_for_loop = range(initial_col, (initial_col + WINNING_STRIKE))
    else:                                                         # left diagonal check
        initial_condi = initial_col >= (WINNING_STRIKE - 1)
        range_for_loop = np.flip(range((initial_col - WINNING_STRIKE + 1), initial_col+1))

    loop_index = 0
    if not (initial_condi and (NUM_ROWS - initial_row >= WINNING_STRIKE)):
        return EMPTY_CELL_VALUE  # no successful diag combo
    else:
        for curr_col in range_for_loop:
            if board[initial_row + loop_index, curr_col] != curr_player_mark:
                return EMPTY_CELL_VALUE  # no successful down combo
            loop_index += 1
        return curr_player_mark  # current player has a successful down diagonal combo



if __name__ == '__main__':
    just_a_change = 5
    game_over_flag = False
    board_game = creat_board()
    print(board_game)
    print("\n")
    while not game_over_flag:

        for curr_player in range(NUM_OF_PLAYERS):
            if not game_over_flag:
                print(f"player {curr_player} what is your move?")
                curr_row_num, curr_col_num = play_turn(board_game)
                board_game[curr_row_num, curr_col_num] = PLAYER_MARKS[curr_player]
                print(board_game)
                winner = is_game_over(board_game)
                if winner != EMPTY_CELL_VALUE:
                    print(f"the winner is player number {winner}")
                    game_over_flag = True





