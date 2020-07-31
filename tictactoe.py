##name: Swapnil Srivastava
##tictactoe.py
##
##problem: This program creates a tictactoe board and asks the user
##              for input of the position they want their
##              character("x" or "o") to be entered. It then enters
##              it and the game is played till there is a winner or
##              all positions on the board are filled.
##
##Certificate of Authenticity:
##    I certify that this is entirely my own work.

#Function to build the board
def buildList():
    theList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return theList

#function to display the tictactoe board
def createBoard(thelist):
    print(thelist[0], "|", thelist[1], "|", thelist[2])
    print("---------")
    print(thelist[3], "|", thelist[4], "|", thelist[5])
    print("---------")
    print(thelist[6], "|", thelist[7], "|", thelist[8])

##function to check if a chosen spot is legal
def legalSpot(board, spot):
##check if the spot is already filled or if the spot exists
    if board[spot-1]!=str("X") and board[spot-1]!=str("O") and (spot<=9
    and spot>=1):
        return True
    else:
        return False

#function to fill a chosen spot
def fillspot(mylist, spot, character):

#check if it is a legal spot
    if legalSpot(mylist, spot) == True:
#fill the legal spot
        mylist[spot-1] = character
    else:
#if it is not legal then print "invalid"
        print("invalid spot")

#fuction to check if the game has been won
def win(board):
    if board[0]==board[3]==board[6]:
        return True
    elif board[1]==board[4]==board[7]:
        return True
    elif board[2]==board[5]==board[8]:
        return True
    elif board[0]==board[1]==board[2]:
        return True
    elif board[3]==board[4]==board[5]:
        return True
    elif board[6]==board[7]==board[8]:
        return True
    elif board[0]==board[4]==board[8]:
        return True
    elif board[2]==board[4]==board[6]:
        return True
    else:
        return False

#function to check if the game is over
def gameOver(theList):
#check if the game has been won
    if win(theList)==True:
        return True
    else:
        return False

#function to play the game
def playGame():
#build the list
    theList = buildList()
#display the board
    createBoard(theList)
#set the player number
    player = 1
#loop to play the game till it is over
    while player<=9 and gameOver(theList)==False:
#get input of the spot to be chosen
        spot = int(input("enter position: "))
#check for spot legality and then fill the spot
        if (spot<=9 and spot>=1) and legalSpot(theList, spot)== True:
#determine the player number
            if player%2 == 1:
                   fillspot(theList, spot, "X")
            else:
                    fillspot(theList, spot, "O")
        else:
                print("enter legal position")
                player -= 1
        player += 1
##        build the new board
        createBoard(theList)
##once the game is over, display results
    if player==10:
        print("Tie")
    elif win(theList)==True:
        print("Player ", player%2 + 1, "Wins!")
        
playGame()
