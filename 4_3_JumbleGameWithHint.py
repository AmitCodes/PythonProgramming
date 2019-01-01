# Here if the user is not able to guess the word will be prompted a hint.
# If the user guessses the word without hint gets a better score compared to with hint
# The hint will be given after some wrong attempts

import random as rand

WORDS = ("language","program","modules","python","tuples")
HINTS = ("Python is a form of it" ,
         "Python is a form of it" ,
         "Python handles various funtionalities using this",
         "A programming Language",
         "A type of collection")
WRONGATTEMPTSALLOWED = 3
totalScore = 0
for i in range(len(WORDS)):
    word = WORDS[i]
    current = word
    # Jumble the word
    jumble = ""
    ErrorAttempts = 0
    while(word):
        randomIndex = rand.randrange(len(word))
        jumble += word[randomIndex]
        word = word[:randomIndex] + word[randomIndex+1:]
    #Prompt the user to guess
    print("The jumbled word is ",jumble)
    print("if you answer this in three attempts you get a score of four else will be given a hint"\
          "later to which you get a score of two")
    #make the user to guess
    guess = None
    hintReceived = False
    while(guess != current):
        if(ErrorAttempts == WRONGATTEMPTSALLOWED):
            print("Hint for the word is",HINTS[i])
            hintReceived = True
        guess = input("Enter the correct Word")
        ErrorAttempts += 1

    if(hintReceived):
        totalScore += 2
        print("You used the hint and thus the score given is 2")
    else:
        totalScore += 4
        print("You did it without hint and thus you get a score of 4")

    if (i != len(WORDS)-1):
        print("You have guessed this correct , moving to the next word")
        print("Your total score as of now is ",totalScore)
    else:
        print("You have finished the game")
        print("Your final score is ",totalScore)
        input("press enter to exit the program")







