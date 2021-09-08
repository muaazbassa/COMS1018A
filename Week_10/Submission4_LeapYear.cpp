//Mu'aaz Bassa
//Submission 4: Leap Year
#include <iostream>
using namespace std;

int main()
{
    int iYear;
    bool bLeapYear;
    cin >> iYear;
    bLeapYear = false;
    if ((iYear % 100) == 0)
    {
        if ((iYear % 400) == 0)
        {
            bLeapYear = true;
        }
    }
    if ((iYear % 100) > 0)
    {
        if ((iYear % 4) == 0)
        {
            bLeapYear = true;
        }
    }
    if (bLeapYear)
    {
        cout << iYear << " is a leap year";
    }
    else
    {
        cout << iYear << " is not a leap year";
    }
    return 0;
}