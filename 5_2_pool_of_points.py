# This program  contains a pool of 30 points.
# All the 30 points can be invested on any of the attributs available.
# This program allows you to take the points from the pool to be added in to any of the attribute or to
# remove the points and push it back to the pool.

attributes = ("Strength","Health","Wisdom","Dexterity")
attributesMap = {"Strength":0,"Health":0,"Wisdom":0,"Dexterity":0}
choices = ("1 - Assign value" , "2 - Remove value","3 - Print the values","4 - Exit the program")

print("The choices available for you are",choices)
poolAmount = 30
oprChoice = int(input("Enter your choice for the action which needs to be done"))
while(oprChoice):

    if(oprChoice > 4):
        print("Wrong choice Selected , Select again")
        print("The choices available for you are", choices)
        oprChoice = int(input("Enter your choice for the action which needs to be done "))
        continue

    print("Enter on what attribute you would like to modify ,",
          "need to provide the index of the value which starts from 1")
    print("Attributes are : " ,attributesMap.keys())
    print("The amount remaining in the pool is ",poolAmount)

    oprChoice -= 1

    if(oprChoice == 0):
        attrChoice = int(input("Enter the attribute index you want to modify"))
        if (attrChoice > 4):
            print("The choice is not possible, please enter again")
            continue

        attrChoice -= 1
        amnt = int(input("Enter the amount"))
        if(poolAmount - amnt < 0):
            print("You have gone or may go out of pool amount , please try again")
        else:
            poolAmount -= amnt
            if(attributes[attrChoice] in attributes):
                attributesMap[attributes[attrChoice]] += amnt
    elif(oprChoice == 1):
        attrChoice = int(input("Enter the attribute index you want to modify"))
        if (attrChoice > 4):
            print("The choice is not possible, please enter again")
            continue

        attrChoice -= 1
        amnt = int(input("Enter the amount to be removed"))
        if (attributes[attrChoice] in attributes and attributesMap[attributes[attrChoice]] - amnt >= 0):
            attributesMap[attributes[attrChoice]] -= amnt
            poolAmount += amnt
        else:
            print("The amount you want to reduce is not possible")
    elif(oprChoice == 2):
        print(attributesMap.items())
    elif(oprChoice == 3):
        print("Exiting the program")
    else:
        print("Wrong option selected , please enter again")

    print("The choices available for you are", choices)
    oprChoice = int(input("Enter your choice for the action which needs to be done "))