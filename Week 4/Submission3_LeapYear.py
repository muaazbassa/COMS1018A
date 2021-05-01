# Mu'aaz Bassa
# Submission 3: Leap Year
iYear = int(input())

bLeapYear = False

if iYear % 100 == 0:
    if iYear % 400 == 0:
        bLeapYear = True

if iYear % 100 > 0:
    if iYear % 4 == 0:
        bLeapYear = True

if bLeapYear:
    print(iYear, "is a leap year")
else:
    print(iYear, "is not a leap year")