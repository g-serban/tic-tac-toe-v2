list_of_lists = [['x', 'y', 'z'], [4, 5, 6], [7, 8, 9]]

def loop(thing):

    for list in thing:
      for element in list:

        print(list, 'list')
        print(element, 'element')
        if element == '7':
            print('true')
    return True


print(loop(list_of_lists))