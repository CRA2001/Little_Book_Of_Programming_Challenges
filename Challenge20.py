'''
Create a Fibonacci sequence generator. (The Fibonacci sequence was originally used as a basic model
for rabbit population growth). The Fibonacci sequence goes like this.
0,1,1,2,3,5,8,13
The Nth term is the sum of the previous two terms. So in the
example above the next term would be 21 because it would be the
previous two terms added together (8+13).
You will need create a list of Fibonnaci numbers up to the 50th
term.
The program will then ask the user for which position in the sequence they want to know the Fibonacci value for (up to 50).
E.g
Which position in sequence? 6 (start counting at 0)
Fibonacci number is 8 
'''

import random 
#used to create the sequence
def createFib():
    li = [0,1]
    #creating the list of fib
    while(len(li)<50):
        val = li[-1] + li[-2]
        li.append(val)

    return li

def findFib(fib):
    pos = int(input("Which position in sequence? \n \t"))
    print("Fibonacci number is {}".format(fib[pos]))
    return 0
findFib(createFib())