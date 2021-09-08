//Mu'aaz Bassa
//Submission 3: Grading

#include <iostream>
using namespace std;

int main() {
    double x;
    cin >> x;
    if (x>=75)
    {
       cout << "First";         
    }
    else if (x>=70 && x<=74)
    {
        cout << "Upper second"; 
    }
    else if (x>=60 && x<=69)
    {
        cout << "Lower second"; 
    }
    else if (x>=50 && x<=59)
    {
        cout << "Third"; 
    }
    else
    {
        cout << "Fail"; 
    }
    return 0;
}