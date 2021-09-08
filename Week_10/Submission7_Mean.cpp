//Mu'aaz Bassa
//Submission 7: Mean
#include <iostream>
using namespace std;

int main() {
    double x,sum,average;
    int iCount=0;
    sum=0;
    cin >> x;
    while (x!=-1)
    {
        sum=sum+x;
        iCount=iCount+1;
        cin >> x;
    }
    average=sum/iCount;
    cout << average;
    return 0;
}