//The Fifth Task
#include <iostream>
#include <string>
#include <vector>
using namespace std;

char ASCII(char letter){
    char x = letter-65;
    return x;
}
void Encrpty(vector<int>&x, vector<int>&y){
    int letters;
    vector<int>output;
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

void Decrypt(vector<int>&x, vector<int>&y){
    int letters;
    vector<int>output;
    int j=1;
    int size;
    size = x.size();
   for (int i = 0; i <y.size();i++){
        if(j>size){
            j=1;
        } 
       letters=y[i]-x[j-1];
       if (letters < 0){
        letters = letters + 26;
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
    string type,codeword,message;
    vector<int>vcodeword,vmessage;
    cin>>type;
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
    //cout<< endl;
    for (int i = 0; i < vmessage.size(); i++)
    {
        //cout<<vmessage[i]<<" ";  
    }
    //cout << endl;
    if (type=="encrypt"){
        Encrpty(vcodeword,vmessage);
    }
    else{
        Decrypt(vcodeword,vmessage);
    }
    return 0;
}
