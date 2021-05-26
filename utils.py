

def are_moves_left(brd):

    for list in brd:
        for element in list:

            if element == '_':
                return True

    return False


def evaluate(b, computer, opponent):
    # Checking for Rows for X or O victory.
    for row in range(3):

        if (b[row][0] == b[row][1]) and (b[row][1] == b[row][2]):
            if b[row][0] == computer:
                return 10

            elif b[row][0] == opponent:
                return -10

    # Checking for Columns for X or O victory.
    for col in range(3):

        if (b[0][col] == b[1][col]) and (b[1][col] == b[2][col]):
            if b[0][col] == computer:
                return 10

            elif b[0][col] == opponent:
                return -10

    # Checking for Diagonals for X or O victory.
    if (b[0][0] == b[1][1]) and (b[1][1] == b[2][2]):
        if b[0][0] == computer or b[1][1] == computer or b[2][2] == computer:
            return 10

        elif b[0][0] == opponent or b[1][1] == opponent or b[2][2] == opponent:
            return -10

    elif (b[0][2] == b[1][1]) and (b[1][1] == b[2][0]):
        if b[0][2] == computer or b[1][1] == computer or b[0][2] == computer:
            return 10

        elif b[0][2] == opponent or b[1][1] == opponent or b[0][2] == opponent:
            return -10

    # Else if none of them have won then return 0
    return 0


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
                    brd[i][j] = computer
                    best = max(best, (minimax(brd, depth + 1, not is_maximizer,
                                              computer, opponent)) - depth)

                    brd[i][j] = '_'

        return best

    else:
        best = 1000

        for i in range(3):
            for j in range(3):

                if brd[i][j] == '_':
                    brd[i][j] = opponent
                    best = min(best, (minimax(brd, depth + 1, not is_maximizer,
                                              computer, opponent)) + depth)

                    brd[i][j] = '_'

        return best
