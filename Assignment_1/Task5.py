#Mu'aaz Bassa
#Assignment 1: Task 5

A=str(input())
B=str(input())
C=str(input())
D=str(input())

def Step1(x,y):
    output=""
    for i in range(0,4):
        if x[i]==y[i]:
            output=output+"0"
        else:
            output=output+"1" 
    return output

E=Step1(A,B)
F=Step1(C,D)
G=Step1(E,F)

def SideWays(x, y, z, w, i):
    output=""
    output=x[i]+y[i]+z[i]+w[i]
    return output

H=SideWays(A,B,C,D,0)
I=SideWays(A,B,C,D,1)
J=SideWays(A,B,C,D,2)
K=SideWays(A,B,C,D,3)

L=Step1(H,I)
M=Step1(J,K)
N=Step1(L,M)
O=Step1(G,N)
P=Step1(O,A)

print(A)
print(B)
print(C)
print(D)
print(E)
print(F)
print(G)
print(H)
print(I)
print(J)
print(K)
print(L)
print(M)
print(N)
print(O)
print(P)
