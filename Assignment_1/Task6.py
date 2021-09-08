#Mu'aaz Bassa
#Assignment 1: Task 6

A=str(input())
B=str(input())
C=str(input())
D=str(input())
E=str(input())
F=str(input())
G=str(input())
H=str(input())
I=str(input())
J=str(input())
K=str(input())
L=str(input())
M=str(input())
N=str(input())
O=str(input())
P=str(input())

def SymbolTable(x):
    if x =="0000":
        output="People"
    elif x=="0001":
        output="Sorrow"
    elif x=="0010":
        output="White"
    elif x=="0011":
        output="Greater Fortune"
    elif x=="0100":
        output="Red"
    elif x=="0101":
        output="Gain"
    elif x=="0110":
        output="The Conjunction"
    elif x=="0111":
        output="Head of the Dragon"
    elif x=="1000":
        output="Joy"
    elif x=="1001":
        output="The Prison"
    elif x=="1010":
        output="Loss"
    elif x=="1011":
        output="The Girl"
    elif x=="1100":
        output="The Lesser Fortune"
    elif x=="1101":
        output="The Boy"
    elif x=="1110":
        output="Tail of the Dragon"
    elif x=="1111":
        output="The Way"
    return output

HouseName=["Life","Riches","Brothers","Father","Sons","Health","Spouse","Death","Journeys","Kings","Good Fortune","Prison","Witness 1","Witness 2","Judge","Reconciler"]

def Houselength(x):
    output=""
    if (len(HouseName[x])>=8):
        output = HouseName[x]+"\t"
    else:
        output = HouseName[x]+"\t\t"
    return output

print("House\t\tName\t\tSymbol")
print("1\t\t"+Houselength(0)+SymbolTable(K))
print("2\t\t"+Houselength(1)+SymbolTable(J))
print("3\t\t"+Houselength(2)+SymbolTable(I))
print("4\t\t"+Houselength(3)+SymbolTable(H))
print("5\t\t"+Houselength(4)+SymbolTable(D))
print("6\t\t"+Houselength(5)+SymbolTable(C))
print("7\t\t"+Houselength(6)+SymbolTable(B))
print("8\t\t"+Houselength(7)+SymbolTable(A))
print("9\t\t"+Houselength(8)+SymbolTable(M))
print("10\t\t"+Houselength(9)+SymbolTable(L))
print("11\t\t"+Houselength(10)+SymbolTable(F))
print("12\t\t"+Houselength(11)+SymbolTable(E))
print("13\t\t"+Houselength(12)+SymbolTable(N))
print("14\t\t"+Houselength(13)+SymbolTable(G))
print("15\t\t"+Houselength(14)+SymbolTable(O))
print("16\t\t"+Houselength(15)+SymbolTable(P))
