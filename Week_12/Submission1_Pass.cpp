//Mu'aaz Bassa
//Submission 1: Pass
#include <iostream>
#include <array>
using namespace std;

int main() {
    //input
    array<int,10>x;
    for (int i = 0; i < x.size(); ++i){
        cin >> x[i];
    }
    int w;
    cin>>w;
    int count=0;
    for (size_t j = 0; j < x.size(); ++j){
        if (x[j]>=w){
            count++;
        }
    }
    cout << count;
    return 0;
}