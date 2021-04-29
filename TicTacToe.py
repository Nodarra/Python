#Board#
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


game_on = True

winner = None

current_player = "O"


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():
    display_board()

    while game_on:
        flip_player()

        handle_turn(current_player)

        check_if_game_over()

    if winner == "X" or winner == "O":
        print(winner + " won!!!")
    elif winner == None:
        print("Tie")


def handle_turn(player):
    print(player + "'s turn.")
    position = input("Choose a postion from 1 to 9: ")

    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        position = input("Choose position from 1 to 9: ")

    position = int(position) - 1

    if board[position] == '-':
        board[position] = player
    else:
        flip_player()
        return
    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    #Set up global variable#
    global winner

    # check rows
    row_winner = check_rows()
    # check compile
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


def check_rows():
    global game_on

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_on = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    global game_on

    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_on = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


def check_diagonals():
    global game_on

    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    if diagonal_1 or diagonal_2:
        game_on = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]

    return


def check_if_tie():
    global game_on

    if "-" not in board:
        game_on = False
    return


def flip_player():
    global current_player

    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'
    return


play_game()
