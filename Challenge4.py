'''
Write a program that will workout the distance
travelled if the user enters in the speed and the time.

Extension:
Get the program to tell you the speed you would have to travel at in order
to go a distance within a certain time entered by the user.
'''

speed = int(input('Enter the speed: '))
time = int(input('Enter the time: '))
distance = speed*time
print('Distance: ',distance)
distance= int(input('Enter the distance: '))
speed = distance/time
print("Speed: ",speed)