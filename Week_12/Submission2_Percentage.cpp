//Mu'aaz Bassa
//Submission 2: Percentage
#include <iostream>
#include <array>
#include <vector>
#include<numeric>
using namespace std;

int main() {
    int x;
    int iTotal;
    int size;
    cin>>size;
    vector<int> vec;
    for (int i = 0; i < size; ++i){
        cin >> x;
        vec.push_back(x);
    }
    /*for (int e : vec){
    cout << e << endl;
    }*/
    //cin>>x;
    //vector<int> vec(x);
    /*for (int i = 0; i < vec.size(); ++i){
        cin >> vec[i];
    }*/
    double q;
    iTotal=accumulate(vec.begin(),vec.end(),0);
    for (int i = 0; i < vec.size(); ++i){
        q = vec[i];
        cout << q/iTotal <<endl;
    }
    //cout << q/iTotal;
    return 0;
}