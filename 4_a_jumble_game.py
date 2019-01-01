# This progmrame jumbles a word and asks for the player to guess the correct word.
# The word is chosen from a collection(which is a tuple).

import random as rand

# WORDS in upper case as it is a constant
WORDS = ("python","program","easy","tuples","dictionary")
# select a word from the collection
# using the random function
# Here the choice function randomly
# picks the element from a collection
word = rand.choice(WORDS)
current = word
# Now the word needs to be jumbled
jumble = ""
while word:
    randomIndex = rand.randrange(len(word))
    jumble += word[randomIndex]
    # I am recreating the word removing the character
    # which got included in the jumble string above
    word = word[:randomIndex] + word[randomIndex+1:]

# now we prompt the user the jumbled
# word and make him/her guess
print("The jumbled word is ", jumble)
guess = None
while(guess != current):
    guess = input("Please enter the correct word ")

print("You have guessed it correct")
