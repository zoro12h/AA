from IPython.display import clear_output


def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])


test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']


def player_input():
    marker = ""
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O?').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark))


import random


def choose_first():
    if random.randint(0, 1) == 0:
        return "player 2"
    else:
        return "player 1"


def space_check(board, position):
    return board[position] == " "


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return True

    return False


def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input("choose a position: (1-9) "))
    return position


def replay():
    choice = "wrong"
    while choice not in ["y", "n"]:
        choice = input("keep playing? (y or n) ")
        if choice not in ["y", "n"]:
            print("sorry, I don't understand, please choose Y or N")
    if choice == "y":
        return True
    else:
        return False


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(f'{turn} will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            print(display_board(theBoard))
            position = player_choice(theBoard)
            print(position)
            print(place_marker(theBoard, player1_marker, position))

            if win_check(theBoard, player1_marker):
                print(display_board(theBoard))
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    print(display_board(theBoard))
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            print(display_board(theBoard))
            position = player_choice(theBoard)
            print(position)
            print(place_marker(theBoard, player2_marker, position))

            if win_check(theBoard, player2_marker):
                print(display_board(theBoard))
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    print(display_board(theBoard))
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
