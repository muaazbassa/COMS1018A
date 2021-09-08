#Mu'aaz Bassa
#Assignment 1: Task 4

x=str(input())
y=str(input())
z=str(input())
w=str(input())

def SideWays(x, y, z, w, i):
    output=""
    output=x[i]+y[i]+z[i]+w[i]
    return output

for i in range(0,4):
    print(SideWays(x,y,z,w,i))
    