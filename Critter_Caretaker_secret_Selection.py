#This program makes a critter caretaker where you can feed the critter.
# Also can check its mood which are calculated considering its hunger and its boredom level.
# Can also print the object values using a secret key 7

class Caretaker:
    def __init__(self,name):
        self.__boredom = 0
        self.__hunger = 0
        self.__name = name
    @staticmethod
    def printMessage():
        print("This is critter care taker game")
        print("Please enter your choice as mentioned below to interact with the critter")
        print(" Enter 1 to 'Play' , Enter 2 to feed , Enter 3 to check its mood , Enter 4 to exit ")

    def getChoice(self):
        inp = int(input("Enter your choice"))  # inp is an integer
        return inp

    def feed(self):
        inp = int(input("Enter the amount you would like to feed"))
        self.__hunger -= inp
        self.__critterWorked()

    def play(self):
        min = int(input("Enter the time in minutes you would like to play"))
        self.__boredom -= min
        self.__critterWorked()

    def getMood(self):
        moodLevel = self.__hunger + self.__boredom
        if(moodLevel <= 0):
            return str("Happy")
        elif(moodLevel >0 and moodLevel <= 5):
            return str("Ok")
        elif(moodLevel >5 and moodLevel <= 10):
            return str("Sad")
        elif(moodLevel>10):
            return str("Frustrated")

    def __critterWorked(self):
        self.__hunger += 1
        self.__boredom += 1

    def __str__(self):
        print("Here are the internal details for this object")
        return str(("Its name is",self.__name,", boredom level is",self.__boredom,"and hunger level is",self.__hunger))

def startProgram():
    critter = Caretaker("Tommy")
    Caretaker.printMessage()
    inp = int(critter.getChoice())
    while (inp != 4):
        if(inp == 1):
            critter.play()
        elif (inp == 2):
            critter.feed()
        elif (inp == 3):
            print("the critter is ", critter.getMood())
        elif (inp == 7):
            print(critter)
        Caretaker.printMessage()
        inp = critter.getChoice()

