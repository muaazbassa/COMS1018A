# Mu'aaz Bassa
# Submission 2: Grading

iGrade = int(input())

if iGrade >= 0 and iGrade <= 100:
    if iGrade >= 75:
        print("First")
    elif (iGrade >= 70) and (iGrade <= 74):
        print("Upper second")
    elif iGrade >= 60 and iGrade <= 69:
        print("Lower second")
    elif iGrade >= 50 and iGrade <= 59:
        print("Third")
    else:
        print("Fail")
