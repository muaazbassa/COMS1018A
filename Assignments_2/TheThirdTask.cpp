//The Third Task
#include <iostream>
#include <string>
#include <vector>
using namespace std;

char ASCII(char letter){
    char x = letter-65;
    return x;
}
void Encrpty(vector<int>&x, vector<int>&y){
    //int j=0;
    int letters;
    vector<int>output;
    /*for (int i = 0; i <x.size(); i++){
        letters=x[i]+y[j];
      if (letters > 90){
       letters = letters - 90;
       }
        output.push_back(letters);
        j++;
        if(i>x.size()){
            i=0;
        }
    }*/
    int j=1;
    int size;
    size = x.size();
   for (int i = 0; i <y.size();i++){
        if(j>size){
            j=1;
        } 
       letters=x[j-1]+y[i];
       if (letters > 25){
        letters = letters - 26;
       }
       j++;
       output.push_back(letters); 
    }
    for(int i=0; i<output.size();i++){
        cout<<char(output[i]+65);
        //cout << output[i] <<" ";
    }
}

int main() {
    string codeword,message;
    vector<int>vcodeword,vmessage;
    cin >> codeword;
    for (int i = 0; i < codeword.length(); i++)
    {
        char x = codeword[i];
        vcodeword.push_back(ASCII(x));  
    }
    for (int i = 0; i < vcodeword.size(); i++)
    {
        //cout<<vcodeword[i] <<" ";  
    }
    cin >> message;
    //cout<< endl;
     for (int i = 0; i < message.length(); i++)
    {
        char x = message[i];
        vmessage.push_back(ASCII(x));  
    }
   // cout<< endl;
    for (int i = 0; i < vmessage.size(); i++)
    {
        //cout<<vmessage[i]<<" ";  
    }
    //cout << endl;
    Encrpty(vcodeword,vmessage);
    //ASCII(codeword);
    return 0;
}
