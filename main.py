import numpy as np

# constants
NUM_ROWS = 6  # number of rows
NUM_COLMS = 7  # number of columns
NUM_OF_PLAYERS = 2  # number of players
# values in cells for player each player (must not be non negative and in the length of NUM_OF_PLAYERS)
PLAYER_MARKS = [0, 3]
# value of an empty cell
EMPTY_CELL_VALUE = -1


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


def is_game_over():
    pass


if __name__ == '__main__':
    game_over_flag = False
    board_gama = creat_board()
    print(board_gama)
    print("\n")
    while not game_over_flag:

        for curr_player in range(NUM_OF_PLAYERS):
            print(f"player {curr_player} what is your move?")
            curr_row_num, curr_col_num = play_turn(board_gama)
            board_gama[curr_row_num, curr_col_num] = PLAYER_MARKS[curr_player]
            print(board_gama)
            # check if victory