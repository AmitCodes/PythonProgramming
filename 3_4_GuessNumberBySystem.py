# This programe makes the system guess the number entered by the user

import random as rand

numb = int(input("Enter the number you want me to guess between 1 and 100"))
guess = rand.randrange(1,101)
print(guess)
lower = 0
upper = 100
while(guess != numb):
    if(guess > numb and lower < upper):
        upper = guess-1
        guess = rand.randint(lower,upper)
        print("guessing a lower value")
    elif(guess < numb and lower < upper):
        lower = guess+1
        guess = rand.randint(lower,upper)
        print("guessing higher value")
    else:
        numb = guess
    print("guess is",guess)
print("number guessed , value is",guess)