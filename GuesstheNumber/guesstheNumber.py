#This is a guess the number game

import os
import random

print('Hello, what is your name?')
name=input()
secretNumber=random.randint(1,20)
print("Well,", name, "I am thinking a number between 1 and 20")

#Ask the player to guess max 5 times
for guesstime in range (1,6):
    print("take a guess")
    guess = int(input())
    if guess < secretNumber :
        print("Your guess is too low")
    elif guess > secretNumber :
        print("Your guess is too high")
    else :
        break #this happens when the player has guessed the right number

if guess == secretNumber :
    print("Welldone",name,"! You guessed the right number in", guesstime, "times!")
else:
    print("Nope, the number I was thinking of was:", secretNumber)
          
        
os.system("PAUSE")


#created by Kostas A. 
