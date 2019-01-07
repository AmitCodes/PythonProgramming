# This is a tic-tac-toe game having support of bot or can be played manually
# The player gets the chance first. The player to start gets the "X" symbol by default.
# User enters the index which he/she needs to update.
# The board basically can be accessed entering the index of the place

boardList = ["1","2","3","4","5","6","7","8","9"]
defaultList = ("1","2","3","4","5","6","7","8","9")
player1Turn = False
botGame = False
userSymbol = ""
botSymbol = ""

def displayRules():
    """This function displays the rules which needs to be followed to play the game"""
    print("""Enter the index which needs to be filled whenever it is your turn which you will be notified when
                                        playing the game 
                                    This is how the board looks 
                                             1| 2 |3
                                            --|---|--
                                             4| 5 |6
                                            --|---|--
                                             7| 8 |9 
             
where the numbers represets the index which you need to enter during your turn to represent your choice.
If any index is already fillef will be shown by symbol "0" or "X" """)

def AskIfBotGame():
    userChoice = input("Plese let us know if you want to play with a bot /n Enter 'Y' for 'Yes' and 'N' for 'No'")
    global botGame
    if(userChoice == "Y"):
        botGame = True
    else:
        botGame = False

def ifBotGame():
    return botGame

def playerOneTurn():
    return player1Turn

def nextTurn():
    global player1Turn
    player1Turn = not player1Turn

def resetBoard():
    global boardList
    boardList = ["1", "2", "3", "4", "5", "6", "7","8", "9"]

def displayBoard():
    print("\t %s| %s |%s "%(boardList[0],boardList[1],boardList[2]))
    print("\t--|---|--")
    print("\t %s| %s |%s "%(boardList[3],boardList[4],boardList[5]))
    print("\t--|---|--")
    print("\t %s| %s |%s "%(boardList[6],boardList[7],boardList[8]))

def askIfWantsToStartAndAssignSymbol():
    wantToStart = input("Do you want to start , please enter 'Y' to start else 'N'")
    global player1Turn
    player1Turn = wantToStart == "Y"
    assignSymbol(userWantsToStart = (wantToStart == "Y"))

def assignSymbol(userWantsToStart):
    global userSymbol
    global botSymbol
    if(userWantsToStart):
        userSymbol = "X"
        botSymbol = "O"
    else:
        userSymbol = "O"
        botSymbol = "X"
    print("You have been assigned the symbol",userSymbol, "and player2/bot has the symbo",botSymbol)

def boardIsFull():
    for i in range(0,len(boardList)):
        if(boardList[i] in defaultList):
            return False
    return True

def checkWinner():
    """ This function checks if there is any winner and returns the symbol of the winner. If no one is the winner it returns 'None' """
    symbol = None
    indexesToBeChecked = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for correctIndexes in indexesToBeChecked:
        if(boardList[correctIndexes[0]] == boardList[correctIndexes[1]] == boardList[correctIndexes[2]]):
            symbol = boardList[correctIndexes[0]];
            break;
    return symbol

def isIndexValid(index):
    index = int(index)
    if((index < 0 or index >8) or boardList[index] not in defaultList):
        print("Your entered index is not valid")
        return False
    return True

def botsMove():
    """This will return the index which bot will be chosing"""
    """Our priority should be the corner boxes and then the other boxes"""
    """if there is not index possible it returns -1"""
    #First we need to check if bot can win the game
    indexes = ("0","2","6","8","4","1","3","5","7") # This tuple is in the priority in which we would like to fill the boxes
    for index in indexes:
        # print("Bot Winning Index = ",index)
        if(isIndexValid(index)):
            if(isWinMove(index,botSymbol)):
                return int(index)

    for index in indexes:
        # print("User Winning Index = ",index)
        if(isIndexValid(index)):
            if(isWinMove(index,userSymbol)):
                return int(index)

    for index in indexes:
        # print("Other Index = ",index)
        if(isIndexValid(index)):
            return int(index)
    return -1


def userMove():
    """This will return the index which user will be chosing"""
    index = int(input("Chose your box for the next move"))
    while(not isIndexValid(index-1)):
        index = int(input("Chose your box for the next move"))
    return index

def isWinMove(index,playerSymbol):
    indexesToBeChecked = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]
    index = int(index)
    global boardList
    boardList[index] = playerSymbol
    for i in range(0,8):
        correctIndexes = indexesToBeChecked[i]
        # print("correct indexes are ",correctIndexes)
        if (index in correctIndexes):
            if(boardList[correctIndexes[0]] == boardList[correctIndexes[1]] and boardList[correctIndexes[1]] == boardList[correctIndexes[2]]):
                boardList[index] = str(index + 1)
                return True

    boardList[index] = str(index + 1)
    return False

def startGame():
    resetBoard()
    displayRules()
    AskIfBotGame()
    askIfWantsToStartAndAssignSymbol()
    index = 10
    while(checkWinner() == None and not boardIsFull()):
        displayBoard()
        if(player1Turn):
            print("\n\tplayer1 turn")
        else:
            print("\n\tplayer2/bot turn")
        if(ifBotGame()):
            if(player1Turn):
                index = userMove()
            else:
                index = botsMove()
        else:
            index = userMove()
        if(player1Turn):
            boardList[index-1] = userSymbol
        elif(not ifBotGame()):
            boardList[index - 1] = botSymbol
        else:
            boardList[index] = botSymbol
        nextTurn()
    print("Winner is",checkWinner())
    inp = input("Press 1 to continue else press any other to exit")
    if(inp == "1"):
           resetBoard()
           startGame()

startGame()
