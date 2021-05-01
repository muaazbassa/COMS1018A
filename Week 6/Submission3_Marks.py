#Mu'aaz Bassa
#Submission 3: Marks

dName=dict()
lName = []
iInput = int(input())
for i in range(iInput):
    sName = str(input())
    dName[sName]=int(input())

marklist = sorted(dName.items())
sortdict = dict(marklist)
for name, mark in sortdict.items():
  print(name, ":", mark)