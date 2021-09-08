//Mu'aaz Bassa
//Submission 2: Ice-Cream

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    vector<string> IceCream;

    string flavour;
    cin >> flavour;
    
    while (flavour != "end"){
        IceCream.push_back(flavour);
        cin >> flavour;
    }

    sort(IceCream.begin(), IceCream.end());

    for (int i = 0; i < IceCream.size(); ++i){
        int count = 1;
        for (int j = i+1; j < IceCream.size(); ++j){
            if (IceCream[i] == IceCream[j]){
                count += 1;
                IceCream[j] = "0";
            }
        }
        if (IceCream[i] != "0"){
            cout << IceCream[i] << ": " << count << endl;
        }
    }
    return 0;
}