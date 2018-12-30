# This program simulates the flipping of coin hundred times and counts the numner of heads
# and then prints the value
# Here 0 is considered as tail and 1 as head
import random

number = 100
head = 0
while(number > 0):
    num = random.randint(0,1) # one can also use random.randrange(0,2)
    #num = random.randrange(0,2)   // randrange excludes the last value i.e [0,2) 
    print(num)
    if(num == 1):
        head += 1
    number -= 1
print ("Number of heads in the flip are" , head)
