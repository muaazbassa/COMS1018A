#Mu'aaz Bassa
#Submission 3: Upshift

sInput = str(input())
sUpshift = ""

for i in range(len(sInput)):
    if (sInput[i] == "z") or  (sInput[i] == "Z"):
        x=0
    else:
        cNew = ord(sInput[i])+1
        sNew = chr(cNew)
        sUpshift = sUpshift + sNew
print(sUpshift)