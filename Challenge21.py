'''
Write a program that will store names into an array.
As a new name is entered it will be added to the end of the array.
The user can keep adding names until they enter the dummy
value ‘exit’
Once this has been done the program will display any duplicate
names.
E.g.
Enter name: Bill
Enter name: Mary
Enter name: Anisha
Enter name: Mary
Enter name: exit
Mary is a duplicate. 
'''

def fun21():
    li = []
    n = ''
    while(n.lower() != "exit"):
        n = input('Enter name: ')
        li.append(n)
    for i in range(0,len(li)):
        for x in range(i+1,len(li)):
            if(li[i]==li[x]):
                print(li[i]+ " is a duplicate")
                break
                        
            
print(fun21())