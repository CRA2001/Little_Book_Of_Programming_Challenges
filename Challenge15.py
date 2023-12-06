'''
Challenge 15
Write a program to count the number of words in a sentence.
The user enters a sentence.
The program responds with the number of words in the sentence.
Hint
Look for spaces and full stops in the string
'''



def fun15():
    #user enters sentence
    s = input("Enter a sentence:  ")
    #sentence is split up and put into an array
    s_arr = s.split(" ")
    #array length is returned
    return len(s_arr)
fun15()
