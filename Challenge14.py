'''
Write a program for a Higher / Lower guessing game
The computer randomly generates a sequence of up to 10 numbers between 1 and 13. The player each after seeing each number
in turn has to decide whether the next number is higher or lower.
If you can remember Brucie’s ‘Play your cards right’ it’s basically
that. If you get 10 guesses right you win the game.
    Starting number : 12
    Higher(H) or lower(L)? L
    Next number 8
    Higher(H) or lower(L)? L
    Next number 11
    You lose 
'''
import random
def fun14():
    attempts = 10
    #starting_num = random.randint(1,13)
    starting_num = 10
    while(attempts != 0):
        user = int(input("Guess the number: "))
        if(user>starting_num):
            print("Lower")
            attempts -= 1
        if(user<starting_num):
            print("Higher")
            attempts -= 1
        if(user==starting_num):
            print("You win.")
            return "You win."
    return "You lose."

fun14()