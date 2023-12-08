'''
Create a simple treasure hunt game.
Create a two-dimensional array of integers 10 by 10.
In a random position in the array store the number 1.
repeat
Get the user to enter coordinates where they think the treasure is.
If there is a 1 at this position display ‘success’.
Until they find the treasure 
'''
import random
def treasureHunt():
    map = [[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1]]
    row_index = random.randint(0, 9)
    col_index = random.randint(0, 9)
    map[row_index][col_index] = 'x'
    x = 0
    y = 0
    flag = False
    while(flag == False):
        y = int(input('Enter the y coordinate: \n '))
        x = int(input('Enter the x coordinate: \n '))
        
        if('x' in map[y] and map[y][x] != 'x'):
            print("You're close, but not there yet. ")
        elif map[y][x] != 'x':
            print("Found a {} here".format(map[y][x]))
            print('No treasure here :(')
        else:
            flag = True
            
    print('YOU FOUND THE TREASURE!')

treasureHunt()