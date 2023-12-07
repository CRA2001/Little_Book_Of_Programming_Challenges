'''
Write a procedure(sub) drawstars that will draw a sequence of
spaces followed by a sequence of stars. It should accept two parameters—the number of spaces and the number of stars.
E.g
Drawstars(3,5) would produce
_ _ _ * * * * * ( _ indicates a space!)
Use your procedure to draw
 * * *
 * * *
 *
 * * *
* * * * * * *
 * * *
 * *
 * * * *
 
 '''


def drawStars(sp,st):
    li = []
    s=""
    if(sp!=0):
        for i in range(sp):
            li.append(" ")
    for i in range(st):
        li.append("*")
    
    return s.join(li)

print(drawStars(2,3))
print(drawStars(2,3))
print(drawStars(3,1))
print(drawStars(2,3))
print(drawStars(0,7))
print(drawStars(2,3))
print("{0} {1}".format(drawStars(2,1),drawStars(0,1)))
print("{0} {1}".format(drawStars(1,2),drawStars(0,2)))
