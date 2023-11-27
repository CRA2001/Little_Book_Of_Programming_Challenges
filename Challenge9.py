'''
Write a program that will generate playing cards e.g. '9 Hearts',
'Queen Spades', when the return key is pressed.
Rather than generate a random number from 1 to 52. Create two random numbers- one for the suit and one for the card.
'''

#import rand
import random


#return a random number from 0 to 3 for the suits
# return a random number from 0 to 12 for the numbers
'''
print(suits[random.randint(0,3)])
print(numbers[random.randint(0,12)])
'''

# now that those two work I need to have a conditional where if the number is a jack , queen , king or ace it will be <numbers> of <suit>
'''
suit = suits[random.randint(0,3)]
number = numbers[random.randint(0,12)]
if number == 'Jack' or number == 'Queen' or number == 'King' or number == 'Ace':
    print("{} of {}".format(number,suit))
else:
    print("{} {}".format(number,suit))
'''
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
n = ""
while(n != 'exit'):
    n=input("Press enter to generate or enter 'exit' to stop generating.")
    suit = suits[random.randint(0,3)]
    number = numbers[random.randint(0,12)]
    if number == 'Jack' or number == 'Queen' or number == 'King' or number == 'Ace':
        print("{} of {}".format(number,suit))
    else:
        print("{} {}".format(number,suit))

