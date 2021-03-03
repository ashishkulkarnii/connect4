from board import dropCoin
from disp import printNice
from checkb import callCheck

board = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]] 
counter = 1

player1, player2 = 1, 2
while counter < 42:

    if counter % 2 == 1:
        #player1
        c = int(input("enter column to drop coin: "))
        board = dropCoin(board, c, player1)
        printNice(board)
        if callCheck(board) != None:
            print(callCheck(board))
            break
    if counter % 2 == 0:
        #player2
        c = int(input("enter column to drop coin: "))
        board = dropCoin(board, c, player2)
        printNice(board)
        if callCheck(board) != None:
            print(callCheck(board))
            break
    #check(board)
    counter += 1
