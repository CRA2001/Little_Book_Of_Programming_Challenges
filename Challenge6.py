'''
Make a game for seeing how good people are at guessing when 10 seconds have elapsed
'''
import time 
input("Hit enter key when ready")
#User hits enter key
#Time starts
start_time = time.time()
# User hits enter key
input("Hit enter again")
# Seconds return 
end_time = time.time()
elapsed_time = round(end_time-start_time)
if(elapsed_time<10):
    print('you are {} away from 10 seconds.'.format(10-elapsed_time))
elif(elapsed_time==10):
    print('You are right on 10 seconds')
else:
    print('You are {} higher than 10.'.format(elapsed_time-10))
