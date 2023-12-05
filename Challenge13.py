'''
Write a program for a game where the computer generates a random starting number between 20 and 30.
The player and the computer can remove 1,2 or 3 from the number in turns. Something like this...
    Starting number : 25
    How many do you want to remove? 3
    22 left
    Computer removes 2
    20 left
    The player who has to remove the last value to bring the number
    down to 0 is the loser.
    1 left
    Computer removes 1
    You win! 
'''
import random
def fun13():
    starting_num = random.randint(20,30)
    while(starting_num > 0):
        user = int(input('How many do you want to remove? (1,2,3)'))
        if  user not in [1,2,3]:
            print('Invalid number')
        else:
            starting_num = starting_num - user
            print("{} left".format(starting_num))
            if(starting_num<=0):
                print('Computer wins')
            comp = random.randint(1,3)
            starting_num = starting_num-comp
            print('{} left'.format(starting_num))
            if(starting_num<=0):
                print('Computer wins')
    
fun13()