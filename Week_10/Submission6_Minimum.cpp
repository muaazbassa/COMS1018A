//Mu'aaz Bassa
//Submission 6: Minimum
#include <iostream>
using namespace std;

int main() {
    int iMin,x;
    cin >> x;
    iMin=x;
    while (x!=-1)
    {
        if(x<iMin){
            iMin=x;
        }
        cin >> x;
    }
    cout << iMin;
    return 0;
}