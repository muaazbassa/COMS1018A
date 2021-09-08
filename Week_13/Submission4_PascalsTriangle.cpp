//Mu'aaz Bassa
//Submission 4: Pascal’s Triangle

#include <iostream>
using namespace std;

int pascal(int x, int y){
    if (y == 0){
        return 1;
    }
    if (x == y){
        return 1;
    }
    else{
        return pascal(x-1, y-1) + pascal(x-1, y);
    }
}

int main(){
    int x, y;
    cin >> x >> y;

    cout << pascal(x, y) << endl;
}