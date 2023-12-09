'''
Write a program that will generate a random
playing card e.g. ‘9 Hearts’, ‘Queen Spades’
when the return key is pressed.
Rather than generate a random number from 1
to 52. Create two random numbers – one for the
suit and one for the card.
However we don't want the same card drawn twice. Update this
program by using an array to prevent the same card being dealt
twice from the pack of cards.
Convert this code into a procedure ‘DealCard’ that will display the
card dealt or ‘no more cards’.
Call your procedure 53 times! 
'''
import random

cards = []
def genCard():
    global cards
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    n = ""
    while(n != 'exit' ):
        n=input("Press enter to generate or enter 'exit' to stop generating.")
        suit = suits[random.randint(0,3)]
        number = numbers[random.randint(0,12)]
        if number == 'Jack' or number == 'Queen' or number == 'King' or number == 'Ace':
            card = "{} of {}".format(number,suit)

        else:
            card = "{} {}".format(number,suit)
        if card not in cards: 
            cards.append(card)
            print("Dealt card:", card)
        else:
            print("Card already dealt. Try Again.")

    print(cards)
def DealCard():
    global cards
    if cards: print("Dealt card: ", cards.pop(0))
    else:
        print("No more cards.")

genCard()
#Calling procedure 53 times.
for _ in range(53):
    DealCard()
