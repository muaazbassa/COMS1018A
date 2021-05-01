#Mu'aaz Bassa
#Submission 4: Vowel Count

sInput = str(input())
while sInput !="end":
    iVowel = 0
    for i in range(len(sInput)):
        if (sInput[i]=="a" or sInput[i]=="e" or sInput[i]=="i" or sInput[i]=="o" or sInput[i]=="u" or sInput[i]=="A" or sInput[i]=="E" or sInput[i]=="I" or sInput[i]=="O" or sInput[i]=="U"):
            iVowel = iVowel + 1
    sInput = str(input())
    print(iVowel)
