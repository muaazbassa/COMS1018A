#Mu'aaz Bassa (2435368)
#Submission 2: Schmerg

import math
def Schmerg(x,y):
    top = (x*y) + (math.sin(x)*math.cos(x)*math.tan(x)) + ((x+0xff22)/(96*y))
    bottom = (((x**2)*(y**-3)) + math.log(y+12))
    return(top/bottom)

x = float(input())
first = 0.5*x
second = 0.7*x
third = x+1
fourth = x-1

Output1 = Schmerg(first,second)
Output2 = Schmerg(x,Output1)
Output3 = Schmerg(third,fourth)
Output4 = Schmerg(Output2,Output3)

print(Output4)