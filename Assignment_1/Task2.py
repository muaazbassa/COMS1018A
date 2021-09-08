#Mu'aaz Bassa
#Assignment 1: Task 2


def Task1(fInput):
    Binary=""
    count=0
    for i in range(0,len(fInput)):
        if fInput[i] == "-":
            count=count+1
    if (count % 2) == 0:
        Binary = Binary + "0"
    else:
        Binary = Binary + "1"
    return Binary

Output=""
Out=[]
for i in range(0,4):
    Output=""
    for j in range(0,4):
        sInput=input()
        Output=Output +Task1(sInput)
    Out.append(Output)
for i in range(0,4):
    print(Out[i])
