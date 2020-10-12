#this is a Tic Tac Toe game

import random, copy

def drawBoard(board):
    #we use this function in order to print the current board
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


def inputPlayerLetter():
    #Let's the player decide whether he wants to play as 'O' or as 'X'
    #returns a list of the players choice and the computer's letter
    letter = ''
    while not (letter == 'O' or letter == 'X'):
        print('Do you want to be O or X')
        letter = input().upper() #so we use the uppercase

    #the first element in the tuple is the player's letter, the second is the computer's letter
    if letter == 'X':
        return ['X','O']
    else:
        return ['O','X']

def whoPlaysFirst():
    #randomly choose the player who plays first
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    #this function returns true if the player wants to play again
    again = 2
    while not (again == 0 or again == 1):
        print('Do you want to play again? (1 for yes or 0 for no)')
        again = int(input())
    if again == 1:
        return True
    else:
        return False
        

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(board, letter):
    #this function takes the board and the player's letter, returns true if the player has won
    return ((board['top-L'] == letter and board['top-M'] == letter and board['top-R'] == letter) or #checks top line
            (board['mid-L'] == letter and board['mid-M'] == letter and board['mid-R'] == letter) or #checks mid line
            (board['low-L'] == letter and board['low-M'] == letter and board['low-R'] == letter) or #checks low line
            (board['top-L'] == letter and board['mid-L'] == letter and board['low-L'] == letter) or #checks left line
            (board['top-M'] == letter and board['mid-M'] == letter and board['low-M'] == letter) or #checks mid line
            (board['top-R'] == letter and board['mid-R'] == letter and board['low-R'] == letter) or #checks right line
            (board['low-L'] == letter and board['mid-M'] == letter and board['top-R'] == letter) or #checks the diagonal
            (board['low-R'] == letter and board['mid-M'] == letter and board['top-L'] == letter))   #checks the other diagonal

def isSpaceFree(board,move):
    #return True if the passed move is free on the board
    return board[move] ==' '

def getPlayerMove(board):
    #the player types his move
    move = ' '
    while move not in 'top-L top-M top-R mid-L mid-M mid-R low-L low-M low-R'.split() or not isSpaceFree(board, move):
        print('What is your next move? Type: top-,mid-,low-, & L, M, R')
        move = input()
    return move

def isBoardFull(board):
    #returns True if every space on the board has been taken.
    for i in 'top-L top-M top-R mid-L mid-M mid-R low-L low-M low-R'.split():
        if isSpaceFree(board, i):
            return False
    return True

def chooseRandomMoveList(board, movesList):
    #returns a valid move from the passed list on the passed board
    #returns none if there is no valid move
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0 :
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    #the computer does its move
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    #Here follows the AI for the game
    #We check, first, if we can win in the next move
    for i in 'top-L top-M top-R mid-L mid-M mid-R low-L low-M low-R'.split():
        dupe = copy.copy(board)
        if isSpaceFree(dupe,i):
            makeMove(dupe, computerLetter, i)
            if isWinner(dupe, computerLetter):
                return i

    #We check, as a second priority, if the player can win in his next move
    for i in 'top-L top-M top-R mid-L mid-M mid-R low-L low-M low-R'.split():
        dupe = copy.copy(board)
        if isSpaceFree(dupe,i):
            makeMove(dupe, playerLetter, i)
            if isWinner(dupe, playerLetter):
                return i
    
    #Try to take one of the corners, if they are free
    move = chooseRandomMoveList(board, ['top-L', 'top-R', 'low-L', 'low-R'])
    if move!= None:
        return move
            
    #try to take the center
    if isSpaceFree(board, 'mid-M'):
        return 'mid-M'

    #move on one of the sides
    return chooseRandomMoveList(board, ['top-M', 'mid-R', 'mid-L', 'low-M'])


print('Welcome to Tic Tac Toe game')
while True:
    #Reset the board
    theBoard={'low-L' : ' ', 'low-M' : ' ', 'low-R' : ' ',\
              'mid-L' : ' ', 'mid-M' : ' ', 'mid-R' : ' ',\
              'top-L' : ' ', 'top-M' : ' ', 'top-R' : ' '}

    playerLetter,computerLetter = inputPlayerLetter()
    turn = whoPlaysFirst()
    print('The ' + turn + ' will play first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            #player's turn
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Welldone! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a Tie!')
                    break
                else:
                    turn = 'computer'

        else:
            #computer's turn
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('Damn! You have lost the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a Tie!')
                    break
                else:
                    turn = 'player'
                
    if not playAgain():
        break


