def printNice(board):
    board = [x for y in board for x in y]
    print(" CONNECT 4!\n\n"+chr(9312),chr(9313),chr(9314),chr(9315),chr(9316),chr(9317),chr(9318)+"\n{} {} {} {} {} {} {}\n{} {} {} {} {} {} {}\n{} {} {} {} {} {} {}\n{} {} {} {} {} {} {}\n{} {} {} {} {} {} {}\n{} {} {} {} {} {} {}\n".format(*board))
