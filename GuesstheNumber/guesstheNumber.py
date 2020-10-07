#This is a guess the number game

import os
import random

print('Hello, what is your name?')
name=input()
print("Well,", name, "I am thinking a number between 1 and 20")

#Ask the player to guess max 5 times
def minigame():
    secretNumber=random.randint(1,20)
    global again
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
        print("Press 1 to play again or 2 to exit")
        again = input()
    else:
        print("Nope, the number I was thinking of was:", secretNumber)
        print("Press 1 to play again or 2 to exit")
        again = input()
#end of minigame  

minigame()

while True:
    try:
        if int(again) == 1 :
            minigame()
        elif int(again) == 2 :
            print("GoodBye Friend")
            break
        else :
            print("I like you little Rebel, let's play again")
            minigame()
    except :
        print("I like you little Rebel, let's play again")
        minigame()


os.system("PAUSE")


#created by Kostas A. 
