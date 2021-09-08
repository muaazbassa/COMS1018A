//The Second Task
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include<bits/stdc++.h>
#include <charconv>
using namespace std;

void ASCII(string letter)
{
    for (int i = 0; i < letter.length(); i++)
    {
        char x = letter.at(i);
        cout << int(x) - 65 << " ";
    }
}

int main(){
    vector< int >vec;
    string S, T;
    getline(cin, S);
    stringstream X(S);
    while (getline(X, T, ' ')) {
        vec.push_back(stoi(T));
        //cout << T << endl;
    }
    vec.resize(vec.size()-1);
    for(int i = 0; i < vec.size();i++){
       //cout << vec[i] << endl;
       vec[i]=vec[i]+65;
    }
    for(int i = 0; i < vec.size();i++){
       cout << char(vec[i]);
    }
    return 0;
}

