def dropCoin(board, column, player):
    if column < 1 or column > 7:
        return None
    else:   
        for row in range(5, -1, -1):
            if board[row][column - 1] == 0:
                board[row][column - 1] = player
                return board
    return None
