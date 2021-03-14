from board import dropCoin
from disp import printNice
from checkb import callCheck
from os import system, name 
from time import sleep

def clear(): 
    if name == 'nt': 
        _ = system('cls') 

board = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]] 

counter = 1

clear()

print("	Loading.")
sleep(.2)
clear()
print("	Loading..")
sleep(.2)
clear()
print("	Loading...")
sleep(.2)
clear()
print("	Loading....")
sleep(.2)
clear()
print("	CONNECT 4!")
sleep(2)
clear()

player1 = input("Player 1: Choose your character!\n")
player1 = player1[0]
player2 = input("Player 2: Choose your character!\n")
player2 = player2[0]

sleep(2)
clear()

def main():
    
    clear()
    
    global counter
    global board
    
    while counter < 42:

        printNice(board)
        
        if counter % 2 == 1:
            #player1
            print("\nPlayer {}'s Turn!\n".format(player1))
            sleep(1)
            try:
                c = int(input("Enter column to drop coin: "))
            except:
                print("Try again!")
                sleep(2)
                counter -= 1
            else:
                boardx = dropCoin(board, c, player1)
                if boardx != None:
                    clear()
                    printNice(boardx)
                    board = boardx
                    if callCheck(board) != None:
                        print("Player {} is the winner!".format(callCheck(board)))
                        break
                else:
                    print("Try again!")
                    sleep(2)
                    counter -= 1
            counter += 1

        if counter % 2 == 0:
            #player2
            print("\nPlayer {}'s Turn!\n".format(player2))
            sleep(1)
            try:
                c = int(input("Enter column to drop coin: "))
            except:
                print("Try again!")
                sleep(2)
                counter -= 1
            else:
                boardx = dropCoin(board, c, player2)
                if boardx != None:
                    clear()
                    printNice(boardx)
                    board = boardx
                    if callCheck(board) != None:
                        print("Player {} is the winner!".format(callCheck(board)))
                        break
                else:
                    print("Try again!")
                    sleep(2)
                    counter -= 1
            counter += 1
            
        clear()
        
    a = input("Do you want to play again? (Y/n)\n")
    if a == 'Y':
        board = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]] 
        main()

main()
