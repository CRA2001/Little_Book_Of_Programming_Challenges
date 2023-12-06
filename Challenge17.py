'''
Challenge 17
Write a function that will convert a UMS score into a grade. The
function will return ‘A’—> ‘U’.
The function will require a parameter to do its job: the mark
The formula for AS level is >=80% —>‘A’, >=70%—>‘B’, >=60%—>‘C’
etc.
Assume the maximum module mark is 100
Having written the function we want to use it three times.
Write a program with the function that allows the user to enter
two module AS scores and displays the grade. It then adds the two
results together and displays the students overall grade. E.g.
Enter Module 1 result: 78
Enter Module 1 result: 67
Result
Module 1 : B
Module 2: C
AS Level : B
'''
def fun17():
    mod1=int(input('Enter Module 1 result: '))
    mod2=int(input('Enter Module 2 result: '))
    if(mod1>=60 and mod1<70):
        mod1_res = 'C'
    elif(mod1>=70 and mod1<80):
        mod1_res = 'B'
    elif(mod1>=80):
        mod1_res = 'A'
    else:
        mod1_res = 'D'
    if(mod2>=60 and mod2<70):
        mod2_res = 'C'
    elif(mod2>=70 and mod2<80):
        mod2_res = 'B'
    elif(mod2>=80):
        mod2_res = 'A'
    else:
        mod2_res = 'D'
    AS_percent = ((mod1+mod2)/200)*100
    if(AS_percent>=60 and AS_percent<70):
        AS_grade = 'C'
    elif(AS_percent>=70 and AS_percent<80):
        AS_grade = 'B'
    elif(AS_percent>=80):
        AS_grade = 'A'
    else:
        AS_grade = 'D'
    print(" Module 1: {}".format(mod1_res))
    print(" Module 2: {}".format(mod2_res))
    print(" AS grade : {}".format(AS_grade))
fun17()