from random import randrange

from evaluation import evaluate


board = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_']
]


def print_board(brd):
    print(' ' + brd[0][0] + ' | ' + brd[0][1] + ' | ' + brd[0][2] + '        ' + '1' + ' | ' + '2' + ' | ' + '3')
    print(' ' + brd[1][0] + ' | ' + brd[1][1] + ' | ' + brd[1][2] + '        ' + '4' + ' | ' + '5' + ' | ' + '6')
    print(' ' + brd[2][0] + ' | ' + brd[2][1] + ' | ' + brd[2][2] + '        ' + '7' + ' | ' + '8' + ' | ' + '9')


def clear_board(brd):
    for i in range(3):
        for j in range(3):
            brd[i][j] = '_'


def winner(brd, computer, human):
    if ((brd[0][0] == computer) and (brd[0][0] == brd[0][1] == brd[0][2])) or (
         (brd[1][0] == computer) and (brd[1][0] == brd[1][1] == brd[1][2])) or (
         (brd[2][0] == computer) and (brd[2][0] == brd[2][1] == brd[1][2])) or (
         (brd[0][0] == computer) and (brd[0][0] == brd[1][1] == brd[2][2])) or (
         (brd[0][2] == computer) and (brd[0][2] == brd[1][1] == brd[2][0])):

        return 10

    elif ((brd[0][0] == human) and (brd[0][0] == brd[0][1] == brd[0][2])) or (
            (brd[1][0] == human) and (brd[1][0] == brd[1][1] == brd[1][2])) or (
            (brd[2][0] == human) and (brd[2][0] == brd[2][1] == brd[1][2])) or (
            (brd[0][0] == human) and (brd[0][0] == brd[1][1] == brd[2][2])) or (
            (brd[0][2] == human) and (brd[0][2] == brd[1][1] == brd[2][0])):

        return -10


def choose_letter():
    letter = input('Please choose X or 0: ')

    while True:

        if letter == '0':
            return letter

        elif letter == 'X' or letter == 'x':
            return letter

        else:
            letter = 'X'  # default to X if player selects the wrong letter or doesn't select at all
            return letter


def comp_letter(letter):
    if letter == '0':
        computer_letter = 'X'
        return computer_letter
    else:
        computer_letter = '0'
        return computer_letter


def player_move(brd, letter):
    try:
        pos = input('Choose a position between 1-9: ')

    except Exception:
        print('Please choose a number!')

    try:
        if pos == '1' and brd[0][0] == '_':
            brd[0][0] = letter

        elif pos == '2' and brd[0][1] == '_':
            brd[0][1] = letter

        elif pos == '3' and brd[0][2] == '_':
            brd[0][2] = letter

        elif pos == '4' and brd[1][0] == '_':
            brd[1][0] = letter

        elif pos == '5' and brd[1][1] == '_':
            brd[1][1] = letter

        elif pos == '6' and brd[1][2] == '_':
            brd[1][2] = letter

        elif pos == '7' and brd[2][0] == '_':
            brd[2][0] = letter

        elif pos == '8' and brd[2][1] == '_':
            brd[2][1] = letter

        elif pos == '9' and brd[2][2] == '_':
            brd[2][2] = letter

        else:
            print('Position occupied. Try again!')

    except Exception:
        print('Something went wrong. Try again!')


def minimax(brd, depth, is_maximizer, computer, opponent):
    score = evaluate(brd, computer, opponent)

    if score == 10:
        return 10

    elif score == -10:
        return score

    elif are_moves_left(brd) is False:
        return 0

    if is_maximizer:
        best = -1000

        for i in range(3):
            for j in range(3):

                if brd[i][j] == '_':
                    board[i][j] = computer
                    best = max(best, (minimax(board, depth + 1, not is_maximizer,
                                              computer, opponent)) - depth)

                    board[i][j] = '_'

        return best

    else:
        best = 1000

        for i in range(3):
            for j in range(3):

                if brd[i][j] == '_':
                    board[i][j] = opponent
                    best = min(best, (minimax(board, depth + 1, not is_maximizer,
                                              computer, opponent)) + depth)

                    board[i][j] = '_'

        return best


def computer_best_move(brd, computer, opponent):
    best_value = -1000
    move = (-1, -1)

    for i in range(3):
        for j in range(3):

            if board[i][j] == '_':
                board[i][j] = computer
                current_move_value = minimax(brd, 0, False, computer, opponent)

                board[i][j] = '_'

                if current_move_value > best_value:
                    move = (i, j)
                    best_value = current_move_value

    # print('The value of the best move is: ', best_value)
    return move


def computer_move(brd, computer, opponent):
    best_move = computer_best_move(brd, computer, opponent)
    i = best_move[0]
    j = best_move[1]
    brd[i][j] = computer


def is_board_full(brd):
    try:
        for i in range(3):
            for j in range(3):

                if brd[i][j] == '_':
                    return False

    except Exception:
        print('Something went wrong. Try again!')


def are_moves_left(brd):

    for list in brd:
        for element in list:

            if element == '_':
                return True

    return False


def game():
    print('Welcome to Tic Tac Toe')

    human = choose_letter().upper()
    computer = comp_letter(human)

    while True:
        player_move(board, human)
        computer_move(board, computer, human)
        print_board(board)

        if is_board_full(board) is None:
            print('-> It\'s a bloody draw!')
            break

        elif winner(board, computer, human) == -10:
            print(f'-> {human} (you) won this round!')
            break

        elif winner(board, computer, human) == 10:
            print(f'-> {computer} (the machine) won this round!')
            break

    while True:
        play_again = input('-> Wanna play again? Yes/ No: ')

        if play_again.lower() == 'yes' or play_again.lower() == 'y':
            clear_board(board)
            game()

        elif play_again.lower() == 'no' or play_again.lower() == 'n':
            print('Thanks for playing my little game!')
            break


if __name__ == '__main__':
    game()
