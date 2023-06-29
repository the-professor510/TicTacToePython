#tic tac toe
import random

board = [0,0,0,0,0,0,0,0,0]
x = 1
o = -1
empty = 0

win = 1
loss = -1
draw = 0

aiColour = 1

def xORo(input):
    if input == 1:
        return "X"
    elif input == -1:
        return "O"
    else:
        return "-"

def printBoard():
    boardString = "\n"

    for i in range(3):
        for j in range(3):
            boardString += xORo(board[i*3+j])
        boardString += "\n"

    print(boardString)

def checkwin(turn):
    #check if there is a vicoty for a player
    check = 0
    if turn == x:
        check = x
    else:
        check = o
    #check rows
    for i in range(0,3):
        if (board[i*3 + 0] == check and board[i*3 + 1] == check and board[i*3 + 2] == check):
            return 1
        
        if (board[0+ i] == check and board[3+i] == check and board[6+i] == check):
            return 1
        
        if (board[0] == check and board[4] == check and board[8] == check):
            return 1
        
        if (board[2] == check and board[4] == check and board[6] == check):
            return 1
        
    return 0
#end check win

def getMove():
    while(True):
        print("Enter a number between 0 and 9 to make a move")
        print("Each number represents the following squares on the board:")
        print("1|2|3"
        +"\n4|5|6"
        +"\n7|8|9")
        move = input("Enter your move:")
        numberedMove = -1

        try:
            numberedMove = int(move)
        except:
            print("You must enter a number between 1 and 9")
            continue

        numberedMove -=1
        
        if (numberedMove<0 or numberedMove>8):
            print("You must enter a number between 1 and 9")

        if board[numberedMove] == empty:
            return numberedMove
        
        print("Square already taken, choose a different number")
    

def boardFull():
    for i in range(9):
        if board[i] == empty:
            return False
    return True

def gameOver(player):
    if checkwin(player):
        if(player == x):
            print("\nX/player one wins")
            printBoard()
            main()
        if(player == o):
            print("\nO/player two wins")
            printBoard()
            main()

    if boardFull():
        print("\nDraw neither play wins")
        main()


def local():
    turn = 1
    while (True):
        printBoard()
        move = getMove()
        board[move] = turn
        gameOver(turn)
        turn = -turn

def aiMove(turn):
    bestScore = -50000
    bestMove = 0
    for i in range(9):
        if (board[i] == empty):
            board[i] = turn
            score = -negaMax(-turn)
            board[i] =empty

            if (score > bestScore):
                bestScore = score
                bestMove = i

    board[bestMove] = turn
            
def negaMax(turn):
    if (checkwin(aiColour)):
        return 10 *turn
    elif (checkwin(-aiColour)):
        return -10 *turn
    elif boardFull():
        return 0
    
    bestScore = -50000;
    for i in range(9):
        if (board[i] == empty):
            board[i] = turn
            score = -negaMax(-turn)
            board[i] =empty

            if (score > bestScore) :
                bestScore = score
    
    return bestScore

def ai():
    turn = 1
    while(True):
        print("\nDo you want to play as player one or player two?")
        print("Enter '1' to play first, '2' to play second")
        choice = input("Enter here: ")

        if choice == "1":
            aiColour = o
            printBoard()
            break
        elif choice == "2":
            aiColour = x
            printBoard()
            aiMove(turn)
            printBoard()
            turn = -turn
            break
        else:
            print("Enter '1' or '2'")

    while (True):
        
        move = getMove()
        board[move] = turn
        printBoard()
        gameOver(turn)
        turn = -turn

        aiMove(turn)
        printBoard()
        gameOver(turn)
        turn = -turn



def main():
    
    for i in range(9):
        board[i] = empty

    while True:
        print("\nDo want to play a local 2 player game or a game against the AI?")
        print("Enter '0' to play a local 2 player game")
        print("Or enter '1' to play a game against the AI")
        choice = input("Enter here: ")

        if choice == "0":
            local()
        elif choice == "1":
            ai()
        else:
            print("Enter '1' or '0'")

main()