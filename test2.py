def are_moves_left(brd):

    for list in brd:
        for element in list:

            print(list, 'list')
            print(element, 'element')

            if element == ' ':
                print('trueest')
                return True

    return False


board = [
    ['x', 'o', '0'],
    ['o', 'x', '0'],
    [' ', ' ', ' ']
]

print(are_moves_left(board))
