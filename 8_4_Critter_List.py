from Critter_Caretaker_secret_Selection import *
# import sys
# sys.path.append("C:Users\AmitSagar\pycharmProjects\helloWorld\venv\Scripts")
critterList = []
def pushNewIntoList(name):
    crit = Caretaker(name)
    critterList.insert(len(critterList),crit)

def playWithAll():
    for critter in critterList:
        critter.play()

def feedToAll():
    for critter in critterList:
        critter.feed()

def doNothing():
    for critter in critterList:
        critter.doNothing()

def init():
    pushNewIntoList("Johny")
    pushNewIntoList("Charlie")
    pushNewIntoList("Adam")
    print("Enter 1 to feed all , Enter 2 to play with all , Enter 3 to do nothing , Enter 4 to exit")
    inp = int(input("Enter your choice"))
    while(inp != 4):
        if(inp == 1):
            feedToAll()
        elif(inp == 2):
            playWithAll()
        elif(inp == 3):
            doNothing()
        print("Enter 1 to feed all , Enter 2 to play with all , Enter 3 to do nothing , Enter 4 to exit")
        inp = int(input("Enter your choice"))

init()

