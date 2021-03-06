from board import dropCoin
from disp import printNice
from checkb import callCheck

board = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]] 
counter = 1

player1, player2 = 1, 2
while counter < 42:

    if counter % 2 == 1:
        #player1
        print("\n\n------------------------------\nPlayer 1's Turn!\n")
        printNice(board)
        c = int(input("Enter column to drop coin: "))
        boardx = dropCoin(board, c, player1)
        if boardx != None:
            printNice(boardx)
            board = boardx
            if callCheck(board) != None:
                print("Player %d is the winner!" % callCheck(board))
                break
        else:
            print("Try again!")
            counter -= 1
        counter += 1

    if counter % 2 == 0:
        #player2
        print("\n\n------------------------------\nPlayer 2's Turn!\n")
        printNice(board)
        c = int(input("Enter column to drop coin: "))
        boardx = dropCoin(board, c, player2)
        if boardx != None:
            printNice(boardx)
            board = boardx
            if callCheck(board) != None:
                print("Player %d is the winner!" % callCheck(board))
                break
        else:
            print("Try again!")
            counter -= 1
        counter += 1
