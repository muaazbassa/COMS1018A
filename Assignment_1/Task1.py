#Mu'aaz Bassa
#Assignment 1: Task 1

sInput=str(input())
count=0
for i in range(0,len(sInput)):
    if sInput[i] == "-":
        count=count+1
if (count % 2) ==0:
    print(0)
else:
    print(1)