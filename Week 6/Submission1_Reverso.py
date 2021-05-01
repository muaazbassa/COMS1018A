#Mu'aaz Bassa
#Submission 1: Reverso


lList=[]
sInput = str(input())
while sInput !="###":
    lList.append(sInput)
    sInput = str(input())
#for i in range(len(lList)-1,0,1):
    #print(lList[i])
count=len(lList)-1
while count >= 0:
  print(lList[count])
  count = count - 1