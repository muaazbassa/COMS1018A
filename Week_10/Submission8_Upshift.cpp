//Mu'aaz Bassa
//Submission 8: Upshift
#include <iostream>
using namespace std;

int main() {
    string sInput,sUpShift,sNew;
    char cNew;
    int i,x;
    
    cin >> sInput;
    sUpShift="";
    for ( int i = 0; i < sInput.length(); i++)
    {
        cNew=int(sInput[i]+1);
        sNew=cNew;
        sUpShift=sUpShift+sNew;
    }
    cout << sUpShift;
    return 0;
}