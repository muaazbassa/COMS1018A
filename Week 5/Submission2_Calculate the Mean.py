#Mu'aaz Bassa
#Submission 2: Calculate the Mean

rInput = float(input())
rTotal = 0.0
iCount=0

while rInput !=-1:
    rTotal = rTotal + rInput
    iCount = iCount +1
    rInput = float(input())
rMean = rTotal/iCount
print(rMean)