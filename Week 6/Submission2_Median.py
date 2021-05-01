#Mu'aaz Bassa
#Submission 2: Median

unsortedlist=[]
iInput = int(input())
for i in range(iInput):
    unsortedlist.append(int(input()))
sortedList = sorted(unsortedlist)

import statistics

print(statistics.median(sortedList))