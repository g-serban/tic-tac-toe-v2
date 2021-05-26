from utils import minimax


class Board:

    board = [
        ['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_']
    ]

    @staticmethod
    def print_board(brd):
        print(' ' + brd[0][0] + ' | ' + brd[0][1] + ' | ' + brd[0][2] + '        ' + '1' + ' | ' + '2' + ' | ' + '3')
        print(' ' + brd[1][0] + ' | ' + brd[1][1] + ' | ' + brd[1][2] + '        ' + '4' + ' | ' + '5' + ' | ' + '6')
        print(' ' + brd[2][0] + ' | ' + brd[2][1] + ' | ' + brd[2][2] + '        ' + '7' + ' | ' + '8' + ' | ' + '9')

    @staticmethod
    def clear_board(brd):
        for i in range(3):
            for j in range(3):
                brd[i][j] = '_'

    @staticmethod
    def is_board_full(brd):
        try:
            for i in range(3):
                for j in range(3):

                    if brd[i][j] == '_':
                        return False

        except Exception:
            print('Something went wrong. Try again!')


class Human:

    @staticmethod
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

    @staticmethod
    def player_move(brd, letter):
        try:
            pos = input('Choose a position between 1-9: ')

        except Exception:
            print('Please choose a number!')

        try:
            if pos == '1' and brd[0][0] == '_':
                brd[0][0] = letter

                return True

            elif pos == '2' and brd[0][1] == '_':
                brd[0][1] = letter

                return True

            elif pos == '3' and brd[0][2] == '_':
                brd[0][2] = letter

                return True

            elif pos == '4' and brd[1][0] == '_':
                brd[1][0] = letter

                return True

            elif pos == '5' and brd[1][1] == '_':
                brd[1][1] = letter

                return True

            elif pos == '6' and brd[1][2] == '_':
                brd[1][2] = letter

                return True

            elif pos == '7' and brd[2][0] == '_':
                brd[2][0] = letter

                return True

            elif pos == '8' and brd[2][1] == '_':
                brd[2][1] = letter

                return True

            elif pos == '9' and brd[2][2] == '_':
                brd[2][2] = letter

                return True

            else:
                print('Position occupied. Try again!')

        except Exception:
            print('Something went wrong. Try again!')


class Computer:

    @staticmethod
    def comp_letter(letter):
        if letter == '0':
            computer_letter = 'X'
            return computer_letter
        else:
            computer_letter = '0'
            return computer_letter

    @staticmethod
    def computer_best_move(brd, computer, opponent):
        best_value = -1000
        move = (-1, -1)

        for i in range(3):
            for j in range(3):

                if brd[i][j] == '_':
                    brd[i][j] = computer
                    current_move_value = minimax(brd, 0, False, computer, opponent)

                    brd[i][j] = '_'

                    if current_move_value > best_value:
                        move = (i, j)
                        best_value = current_move_value

        # print('The value of the best move is: ', best_value)
        return move

    @staticmethod
    def computer_move(brd, computer, opponent):
        best_move = Computer.computer_best_move(brd, computer, opponent)
        i = best_move[0]
        j = best_move[1]
        brd[i][j] = computer
