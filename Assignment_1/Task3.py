#Mu'aaz Bassa
#Assignment 1: Task 3

output=""
x=str(input())
y=str(input())
for i in range(0,4):
    if x[i]==y[i]:
        output=output+"0"
    else:
        output=output+"1" 
print(output)