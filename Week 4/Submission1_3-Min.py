#Mu'aaz Bassa
#Submission 1: 3-Min

x = float(input())
y = float(input())
z = float(input())

if x <= y:
    rMinimum = x
else:
    rMinimum = y
if z < rMinimum:
    rMinimum = z

print(rMinimum)
