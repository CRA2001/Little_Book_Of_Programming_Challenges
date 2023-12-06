'''
Challenge 16
Guess the number game.
The computer selects a random number between 1 and 100.
The user keeps guessing which number the computer has chosen
until they get it right.
The computer responds ‘got it’ or ‘too high’ or ‘too low’ after each
guess.
After the user has guessed the number the computer tells them
how many attempts they have made. 
'''
import random
def fun16():
    #n = random.randint(1,100)
    n = 64
    s = 0
    guess_count = 0
    while(s!=n):
        guess_count+=1
        s = int(input('Guess the number:  '))
        if(s<n):
            print('Guess is too low.')
        if(n<s):
            print('Guess is too high.')
    return ' YOU GOT IT with {} guesses'.format(guess_count)



print(fun16())