'''use while loop for rock paper scissors against random. best 2 out of 3 wins. if it is a tie it must be replayed and does not count.
first import random
comp = random.randint(0,2)
then ask the user to enter rock,paper,or scissors....cast as int
assign rock = 0, paper = 1, scissors = 2

since the num paper is greater than num rock we can---maybe..

incorporating the while loop to end when total games won by user or comp = 2. other wise use if statements.
USE RANDOM.CHOICE!!!! I.E CHOOSE BETWEEN [ROCK,PAPER, SCISSORS]
MAKE SURE EVERYTHING IS LOWER CASE!'''

import random

#put int(user question here or in loop?)

cwins = 0
uwins = 0

while cwins or uwins != 2:


    comp = random.choice(["rock","paper", "scissors"])
    user = input(str("choose rock, paper, or scissors "))
    print("computer chose" ,comp)


    if cwins or uwins == 2:
        break


    elif user == comp:
        print("its a tie! lets try again")

    elif user == 'rock' and comp == 'scissors' or user == 'paper' and comp == "rock" or user == 'scissors' and comp == 'paper':
        uwins +=1
        print("you win this round")
        print("your total wins =",uwins)
        print("comp total wins = ",cwins)
    else:
        cwins +=1
        print("comp wins this round")
        print("comps total wins =", cwins)
        print("your total wins =",uwins)



print("game over")
print("computer ended up winning",cwins)
print("you ended winning", uwins)
#if uwins == 2:
    #print ("your total wins",uwins)

#if cwins == 2:
    #print("computers total wins",cwins)
