'''
The computer generates a 4 digit code
The user types in a 4 digit code. Their guess.
The computer tells them how many digits they guessed correctly
'''
import random
def fun26():
    #computer generating the four digit code.
    code1 =[random.randint(1,9) for x in range(0,4)]
    #user typing the 4 digit code
    code2 = [int(input("Enter a value from 0 to 9: ")) for x in range(0,4)]
    #checking if the four digit code is correct
    if code1==code2:
        print("Correct guess")
    else:
        count = 0
        for i in range(len(code2)):
            if(code2[i] in code1):
                count+=1
        print("You didn't guess correctly. Digits guessed correctly {} but were not in the correct position.".format(count))
fun26()