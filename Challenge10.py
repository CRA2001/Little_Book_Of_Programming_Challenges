'''
Make a game of rock, paper scissors against the
computer.
Algorithm
  -Tell user to enter either rock,paper or scissors
 -Get the response
 -Generate a random number from 1 to 3 (1=rock,2=paper,3=scissors)
 -Compare user selection and computer selection
 -Display who wins.
'''
import random
n = input('rock,paper or scissors? ')
comp = random.randint(1,3)
if(comp == 1):
    comp = 'rock'
if(comp == 2):
    comp = 'paper'
if(comp == 3):
    comp = 'scissors'

#comp wins    
if (comp=='rock' and n == 'scissors') or (comp == 'scissors' and n =='paper') or (comp == 'paper' and n=='rock'):
    print('Computer wins')
else:
    print('You win')


#you win