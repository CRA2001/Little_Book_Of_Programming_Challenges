'''
Write a program that will give the students the answer to logic gate questions e.g.
    Enter logic gate : OR
    Enter first input : 1
    Enter second input :0
    Result = 1
It should work for the logic gates OR, AND and XOR
'''

def logicGate():
    # Enter gate
    gate = input("Enter Logic Gate: ")
    # Enter first input
    a = int(input("Enter A: "))
    # Enter second input
    b = int(input("Etner B: "))
    # Result 
    result = None
    if gate == 'AND':
        if(a==0 and b==0):
            result = 0
        if(a==1 and b==0):
            result = 0
        if(a==0 and b==1):
            result = 0
        if(a==1 and b==1):
            result == 1

    if gate == 'OR':
        if(a==0 and b==0):
            result = 0
        if(a==1 and b==0):
            result = 1
        if(a==0 and b==1):
            result = 1
        if(a==1 and b==1):
            result == 1


    if gate == 'XOR':
        if(a==0 and b==0):
            result = 0
        if(a==1 and b==0):
            result = 1
        if(a==0 and b==1):
            result = 1
        if(a==1 and b==1):
            result == 0

    if gate == 'NAND':
        if(a==0 and b==0):
            result = 1
        if(a==1 and b==0):
            result = 1
        if(a==0 and b==1):
            result = 1
        if(a==1 and b==1):
            result == 0

    if gate == 'NOR':
        if(a==0 and b==0):
            result = 1
        if(a==1 and b==0):
            result = 0
        if(a==0 and b==1):
            result = 0
        if(a==1 and b==1):
            result == 0

    return result

print(logicGate())