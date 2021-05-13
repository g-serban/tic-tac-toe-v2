from random import randrange


board = [' ' for x in range(10)]
board[0] = '.'


def insert_letter(letter: str, position: int):
    board[position] = letter


def space_is_free(position: int) -> bool:
    return board[position] == ' '


def print_board(brd):
    print('   |   |')
    print(' ' + brd[1] + ' | ' + brd[2] + ' | ' + brd[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + brd[4] + ' | ' + brd[5] + ' | ' + brd[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + brd[7] + ' | ' + brd[8] + ' | ' + brd[9])
    print('   |   |')


def clear_board(brd):
    for i in range(10):
        brd[i] = ' '

    brd[0] = '.'


def is_human_winner(brd, letter):  # TODO can we have only on is_winner function?
    return (brd[1] == letter) and (brd[2] == letter) and (brd[3] == letter) or (
        brd[4] == letter) and (brd[5] == letter) and (brd[6] == letter) or (
        brd[7] == letter) and (brd[8] == letter) and (brd[9] == letter) or (
        brd[1] == letter) and (brd[4] == letter) and (brd[7] == letter) or (
        brd[2] == letter) and (brd[5] == letter) and (brd[8] == letter) or (
        brd[3] == letter) and (brd[6] == letter) and (brd[9] == letter) or (
        brd[1] == letter) and (brd[5] == letter) and (brd[9] == letter) or (
        brd[3] == letter) and (brd[5] == letter) and (brd[7] == letter)


def is_computer_winner(brd, letter):
    return (brd[1] == letter) and (brd[2] == letter) and (brd[3] == letter) or (
        brd[4] == letter) and (brd[5] == letter) and (brd[6] == letter) or (
        brd[7] == letter) and (brd[8] == letter) and (brd[9] == letter) or (
        brd[1] == letter) and (brd[4] == letter) and (brd[7] == letter) or (
        brd[2] == letter) and (brd[5] == letter) and (brd[8] == letter) or (
        brd[3] == letter) and (brd[6] == letter) and (brd[9] == letter) or (
        brd[1] == letter) and (brd[5] == letter) and (brd[9] == letter) or (
        brd[3] == letter) and (brd[5] == letter) and (brd[7] == letter)


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
        pos = int(input('Choose a position between 1-9: '))

    except Exception:
        print('Please choose a number!')

    try:
        if space_is_free(pos):
            brd[pos] = letter

        else:
            print('Position occupied. Try again!')

    except Exception:
        print('Something went wrong. Try again!')


def computer_move(brd, computer_letter):  # TODO instead of having a random move, try to make te computer move smarter!
    random_move = randrange(0, 9)

    for i in list(range(len(brd))):
        if brd[random_move] != 'X' or brd[random_move] != '.':
            brd[random_move] = computer_letter


def is_board_full(brd):
    try:
        for i in list(range(10)):
            if brd[i] == ' ':
                return False

    except Exception:
        print('Something went wrong. Try again!')


def game():
    print('Welcome to Tic Tac Toe')

    human = choose_letter().upper()
    computer = comp_letter(human)

    while True:
        player_move(board, human)
        computer_move(board, computer)
        print_board(board)

        if is_board_full(board) is None:
            print_board(board)
            print('-> It\'s a bloody draw!')
            break

        elif is_human_winner(board, human):
            print_board(board)
            print(f'-> {human} (you) won this round!')
            break

        elif is_computer_winner(board, computer):
            print_board(board)
            print(f'-> {computer} (the machine) won this round!')
            break

    while True:
        play_again = input('-> Wanna play again? Yes/ No: ')

        if play_again.lower() == 'yes':
            clear_board(board)
            game()

        elif play_again.lower() == 'no':
            print('Thanks for playing my little game!')
            break


if __name__ == '__main__':
    game()
