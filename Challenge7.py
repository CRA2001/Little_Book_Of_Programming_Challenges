'''
Extend the one from challenge 5, to make a game for
seeing how quick people are at typing the alphabet.
Algorithm:
1. Tell them to hit enter key when ready.
2. Get the first time in seconds(and minutes).
3. Get them to type in the alphabet and hit enter.
4. Check they have entered the alphabet correctly.
5. If they entered it correctly then 
    i. Subtract first time from the second time
    ii. Tell them how many seconds they took
'''
import time

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
inc_count = 0
cor_count = 0
input('Hit enter when ready...  ')
start_time=time.time()
for i in range(0,len(alphabet)):
    input_let =input("Enter the letter: ")
    if input_let == alphabet[i] or input_let == alphabet[i].lower():
        cor_count+=1
        print("CORRECT")
    else:
        inc_count+=1
        print("INCORRECT")
end_time=time.time()
#show time taken
end_time=time.time()
elapsed_time = round(end_time-start_time)
print('You took {} seconds'.format(elapsed_time))
print('You got {} correct'.format(cor_count))
print('You got {} incorrect'.format(inc_count))
    
        

    