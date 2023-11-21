'''
Write a program to workout how many days you have lived for.
Algorithm:
1. Enter date of birth
2. Get today's date
3. Get the difference in days between the two dates
4. Display result
'''

from datetime import date

year_dob = int(input('Enter year of birth: '))
month_dob = int(input('Enter month of birth: '))
day_dob = int(input('Enter day of birth: '))
dob = date(year_dob,month_dob,day_dob)
today = date.today()
print(today-dob)


