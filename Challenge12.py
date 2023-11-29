'''
Write a program that will display all the factors of a number, entered by the user, that are bigger than 1.
(e.g. the factors of the number 12 are 6,4,3 and 2 because they divide into 12 exactly).
Hint
to find out whether a number X is a factor of Y use :
IF Y mod X =0 (there is nothing remaining when Y is divided by X) 
'''

def factors():
    factors =[]
    n = int(input('Enter factors: '))
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)

    return factors
print(factors())