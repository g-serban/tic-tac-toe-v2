

def evaluate(b):

    # Checking for Rows for X or O victory
    for row in range(0, 3):

        if b[row][0] == b[row][1] and b[row][1] == b[row][2]:
            if b[row][0] == 'x':
                return 10

            elif b[row][0] == '0':
                return -10

    # Checking for Columns for X or O victory
    for col in range(0, 3):

        if b[0][col] == b[1][col] and b[1][col] == b[2][col]:
            if b[0][col] == 'x':
                return 10

            elif b[0][col] == '0':
                return -10

    # CChecking for Diagonals for X or O victory
    if b[0][0] == b[1][1] and b[1][1] == b[2][2]:

        if b[0][0] == 'x':
            return 10

        elif b[0][0] == '0':
            return -10

    if b[0][2] == b[1][1] and b[1][1] == b[2][0]:

        if b[0][2] == 'x':
            return 10

        elif b[0][2] == '0':
            return -10

    # if none have won return 0
    return 0


# driver code
if __name__ == '__main__':

    board = [['x', '_', 'o'],
             ['_', 'x', 'o'],
             ['_', '_', 'x']]

    value = evaluate(board)
    print('The value of this board is: ', value)

