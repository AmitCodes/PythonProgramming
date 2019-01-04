# Here we need to store name of son's father and grandfather.
# Using tha name of the son, one should be able to access father and grafather

#Notify the user for the options available
print("Enter one of the below choices to proceed further")
print("1 - Insert new data" , "2 - Get the data" , "3 - Delete the data","4 - Exit")
choice = int(input("Enter your choice "))
#Creating a basic dictinary which basically maintains the data
relationsDict = {"Raj" : ("Sunil","Param")}
while(choice != 4):
    if(choice == 1):
        son = input("Enter sons name")
        father = input("Enter fathers name")
        grandfather = input("Enter grand fathers name")
        if(son not in relationsDict):
            relationsDict[son] = (father,grandfather)
        else:
            print("relationship already exist")
    elif(choice == 2):
        son = input("Enter the sons name whose relationship needs to be printed")
        if(son in relationsDict):
            father,grandfather = relationsDict[son]
            print(son ,"father's name is",father,"and grandfather's name is",grandfather)
        else:
            print("This name does not exist")
    elif(choice == 3):
        son = input("Enter the sons name which needs to be deleted")
        if(son in relationsDict):
            del relationsDict[son]
        else:
            print("Son's name does not exist")
    elif(choice == 4):
        print("exiting the game")
    else:
        print("wrong choice , please select again")

    print("Enter one of the below choices to proceed further")
    print("1 - Insert new data", "2 - Get the data", "3 - Delete the data", "4 - Exit")
    choice = int(input("Enter your choice "))



