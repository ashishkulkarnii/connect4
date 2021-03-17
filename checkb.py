def checkVertical(board):
    for i in range(0, 3):
        for j in range(0, 7):
            x = board[i][j]
            if x != 0:
                
                if board[i + 1][j] == x and board[i + 2][j] == x and board[i + 3][j] == x:
                    return x

def checkHorizontal(board):
    for i in range(0, 6):
        for j in range(0, 4):
            x = board[i][j]
            if x != 0:
                if board[i][j + 1] == x and board[i][j + 2] == x and board[i][j + 3] == x:    
                    return x

def checkDiagNegative(board):
    for i in range(0, 3):
        for j in range(0, 4):
            x = board[i][j]
            if x != 0:
                if board[i + 1][j + 1] == x and board[i + 2][j + 2] == x and board[i + 3][j + 3] == x:
                    return x

def checkDiagPositive(board):
    for i in range(0, 3):
        for j in range(3, 6):
            x = board[i][j]
            if x != 0:
                if board[i + 1][j - 1] == x and board[i + 2][j - 2] == x and board[i + 3][j - 3] == x:
                    return x

def callCheck(board):
    if checkDiagPositive(board) != None:
        return checkDiagPositive(board)
    if checkHorizontal(board) != None:
        return checkHorizontal(board)
    if checkDiagNegative(board) != None:
        return checkDiagNegative(board)
    if checkVertical(board) != None:
        return checkVertical(board)
