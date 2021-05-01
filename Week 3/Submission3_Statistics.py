#Mu'aaz Bassa
#Submission 3: Statistics
import math
#INPUT
a = float(input())
b = float(input())
c = float(input())
d = float(input())

#Mean
rMean = (a+b+c+d)/4

#var
rVar = (((rMean-a)**2)+((rMean-b)**2)+((rMean-c)**2)+((rMean-d)**2))/4

#std
rStd = math.sqrt(rVar)

#OUTPUT
print(rMean)
print(rVar)
print(rStd)