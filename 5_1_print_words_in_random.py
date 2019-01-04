#This program takes some collection of words in the list
#Then choses each wotd at random and prints it. COndition being each word should be printed only once.

import random as rand
words = ["Python" , "Program" , "is" , "easy"]
while words:
    word = rand.choice(words)
    print(word,end = " ")
    words.remove(word)
