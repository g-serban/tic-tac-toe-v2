from models import Board, Human, Computer


class Game:

    @staticmethod
    def winner(brd, computer, human):
        if ((brd[0][0] == computer) and (brd[0][0] == brd[0][1] == brd[0][2])) or (
             (brd[1][0] == computer) and (brd[1][0] == brd[1][1] == brd[1][2])) or (
             (brd[2][0] == computer) and (brd[2][0] == brd[2][1] == brd[1][2])) or (
             (brd[0][0] == computer) and (brd[0][0] == brd[1][0] == brd[2][0])) or (
             (brd[0][1] == computer) and (brd[0][1] == brd[1][1] == brd[2][1])) or (
             (brd[0][2] == computer) and (brd[0][2] == brd[1][2] == brd[2][2])) or (
             (brd[0][0] == computer) and (brd[0][0] == brd[1][1] == brd[2][2])) or (
             (brd[0][2] == computer) and (brd[0][2] == brd[1][1] == brd[2][0])):

            return 10

        elif ((brd[0][0] == human) and (brd[0][0] == brd[0][1] == brd[0][2])) or (
                (brd[1][0] == human) and (brd[1][0] == brd[1][1] == brd[1][2])) or (
                (brd[2][0] == human) and (brd[2][0] == brd[2][1] == brd[1][2])) or (
                (brd[0][0] == human) and (brd[0][0] == brd[1][0] == brd[2][0])) or (
                (brd[0][1] == human) and (brd[0][1] == brd[1][1] == brd[2][1])) or (
                (brd[0][2] == human) and (brd[0][2] == brd[1][2] == brd[2][2])) or (
                (brd[0][0] == human) and (brd[0][0] == brd[1][1] == brd[2][2])) or (
                (brd[0][2] == human) and (brd[0][2] == brd[1][1] == brd[2][0])):

            return -10

    @staticmethod
    def game():
        print('Welcome to Tic Tac Toe')

        human = Human.choose_letter().upper()
        computer = Computer.comp_letter(human)
        board = Board.board

        while True:
            move = Human.player_move(board, human)

            if move is True:
                Computer.computer_move(board, computer, human)
                Board.print_board(board)

            if Board.is_board_full(board) is None:
                print('-> It\'s a bloody draw!')
                break

            elif Game.winner(board, computer, human) == -10:
                print(f'-> {human} (you) won this round!')
                break

            elif Game.winner(board, computer, human) == 10:
                print(f'-> {computer} (the machine) won this round!')
                break

        while True:
            play_again = input('-> Wanna play again? Yes/ No: ')

            if play_again.lower() == 'yes' or play_again.lower() == 'y':
                Board.clear_board(board)
                Game.game()

            elif play_again.lower() == 'no' or play_again.lower() == 'n':
                print('Thanks for playing my little game!')
                break


if __name__ == '__main__':
    Game.game()
