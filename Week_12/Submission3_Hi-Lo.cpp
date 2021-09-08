//Mu'aaz Bassa
//Submission 3: Hi-Lo
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    double x;
    double size;
    cin>>size;
    vector<double> vec;
    for (int i = 0; i < size; ++i){
        cin >> x;
        vec.push_back(x);
    }
    sort(vec.begin(), vec.end());
    cout << vec[1] <<endl;
    cout << vec[size-2]<<endl;
    return 0;
}