'''
HangMan
Player 1 types in a word
Player 2 has to guess the word in 5 lives
The display would look like this
Word to guess: ******
You have 5 lives left - Letter? E
Word to guess: **EE*E
You have 5 lives left - Letter? Z
Word to guess: **EE*E
You have 4 lives left - Letter? 
'''
def hangMan(word):
    og_word = word
    word = [*word]
    word_covered = ["*" for x in range(len(word))]
    lives = 5
    while(lives>0):
        print("Word to guess: {}".format("".join(word_covered)))
        guess=input("You have {} lives left - Letter? ".format(lives))
        if(guess in word):
            print("Okay you got it right but this part I still gotta code")
            index = word.index(guess)
            word[index]='*'
            word_covered[index]=guess
        else:
            lives -= 1
        if ''.join(word_covered) == og_word:
            break
    if(lives==0):
        print("Bruh.")
    else:
        print("YOU GOT IT.")

hangMan("hello")