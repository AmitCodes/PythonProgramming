import pickle as pick
import os

# Maintain a file which will store the questions and answers
# The file should also maintain a score for each question.
# Also the total score for the session and highest score

def readLine(fileHandle):
    line = fileHandle.readline()
    return line

def welcomeMessage():
    print("Welcome to the puzzle game for Python")
    print("Chose the correct answer for the questions displayed",
          "by writing the option which is correct according to you")

def readNextBlock(fileHandle):
    question = fileHandle.readline()
    if(not question):
        return None,[],None,None
    options = []
    for i in range(4):
        options.insert(i,fileHandle.readline())
    correctAnswer = fileHandle.readline()
    scoreForTheQuestion = fileHandle.readline()
    return (question,options,correctAnswer,scoreForTheQuestion)

def displayQuestion(handle):
    question,options,correctAnswer,scoreForTheQuestion = readNextBlock(handle)
    print(question)
    for i in range(len(options)):
        print(options[i])
    return correctAnswer,scoreForTheQuestion

def highestScoreUpdate(higherScore,username):
    print("function::highestScoreUpdate")
    fileHandle = open("Score.dat","rb+")
    fileHandle.close()
    fileHandle = open("Score.dat","rb")
    higherScore = int(higherScore)
    if(pick.load(fileHandle)):
        fileHandle.close()
        fileHandle = open("Score.dat", "rb")
        print("got into the binary file")
        list1 = pick.load(fileHandle)
        if(int(list1[1]) < higherScore):
            print("Your score",higherScore,"is higher compared to previous score",list1[1])
            fileHandle = open("Score.dat","wb")
            pick.dump([username,higherScore],fileHandle)
    else:
        pick.dump(["username", "0"], fileHandle)

def startGame():
    handle = open("PythonPuzzle.dat")
    welcomeMessage()
    scoreForThisSession = 0
    correct,scoreForTheQuestion = displayQuestion(handle)
    while(correct):
        userOption = int(input("Enter the correct option"))
        if(userOption == int(correct)):
            print("correct answer")
            scoreForThisSession += int(scoreForTheQuestion)
        else:
            print("Wrong answer")
        correct,scoreForTheQuestion = displayQuestion(handle)
    userName = input("Enter you name for the score update")
    highestScoreUpdate(scoreForThisSession,userName)

startGame()