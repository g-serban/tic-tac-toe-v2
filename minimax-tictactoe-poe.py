

player, opponent = 'x', 'o'


def are_moves_left(brd):

    for list in brd:
        for element in list:

            if element == '_':
                return True

    return False


# evaluation function
def evaluate(b):
    # Checking for Rows for X or O victory.
    for row in range(3):

        if (b[row][0] == b[row][1]) and (b[row][1] == b[row][2]):
            if b[row][0] == player:
                return 10

            elif b[row][0] == opponent:
                return -10

    # Checking for Columns for X or O victory.
    for col in range(3):

        if (b[0][col] == b[1][col]) and (b[1][col] == b[2][col]):
            if b[0][col] == player:
                return 10

            elif b[0][col] == opponent:
                return -10

    # Checking for Diagonals for X or O victory.
    if (b[0][0] == b[1][1]) and (b[1][1] == b[2][2]):
        if b[0][0] == player or b[1][1] == player or b[2][2] == player:
            return 10

        elif b[0][0] == opponent or b[1][1] == opponent or b[2][2] == opponent:
            return -10

    elif (b[0][2] == b[1][1]) and (b[1][1] == b[2][0]):
        if b[0][2] == player or b[1][1] == player or b[0][2] == player:
            return 10

        elif b[0][2] == opponent or b[1][1] == opponent or b[0][2] == opponent:
            return -10

    # Else if none of them have won then return 0
    return 0


# minimax function
def minimax(board, depth, is_maximizer):
    score = evaluate(board)

    if score == 10:
        return score

    elif score == -10:
        return score

    elif are_moves_left(board) is False:
        return 0

    if is_maximizer:
        best = -1000

        for i in range(3):
            for j in range(3):

                if board[i][j] == '_':
                    board[i][j] = player
                    best = max(best, minimax(board, depth + 1, not is_maximizer))

                    # undo the move
                    board[i][j] = '_'

        return best

    else:
        best = 1000

        for i in range(3):
            for j in range(3):

                if board[i][j] == '_':
                    board[i][j] = opponent
                    best = min(best, minimax(board, depth + 1, not is_maximizer))

                    # undo the move
                    board[i][j] = '_'

        return best


def find_best_move(board):
    best_val = -1000
    best_move = (-1, -1)

    # traverse all cells, evaluate minimax function for all empty cells.
    # return cell with optimal value

    for i in range(3):
        for j in range(3):

            if board[i][j] == '_':
                board[i][j] = player
                move_val = minimax(board, 0, False)

                # undo the move
                board[i][j] = '_'

                # if value of current move is more than the best value, then update best
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    print('The value of the best move is: ', best_val)
    print()
    return best_move


board = [
    ['o', 'x', 'o'],
    ['x', 'o', '_'],
    ['x', 'x', 'x']
]

best_move = find_best_move(board)

print('the optimal move is: ')
print("ROW:", best_move[0], " COL:", best_move[1])










