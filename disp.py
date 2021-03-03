def printNice(board):
    board = [x for y in board for x in y]
    print("{} {} {} {} {} {} {}\n{} {} {} {} {} {} {}\n{} {} {} {} {} {} {}\n{} {} {} {} {} {} {}\n{} {} {} {} {} {} {}\n{} {} {} {} {} {} {}\n".format(*board))
