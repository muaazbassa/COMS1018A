//Mu'aaz Bassa
//Submission 1: Upper Case
#include <iostream>
#include <string>
using namespace std;

void Uppercase(string up) {
    //cout << "Original String:\n"<< up<< endl;
    //cout<<"String in UPPERCASE:\n";
    for (int x=0; x<(up).length(); x++)
        putchar(toupper(up[x]));
        cout<< endl;
}

int main() {
    int j;
    cin>> j;
    for (int i = 0; i < j+1; i++)
    {
        string sInput;
        cin>>sInput;
        Uppercase(sInput);
    }
    return 0;    
    
}