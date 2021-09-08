//The Sixth Task
#include <iostream>
#include <string>
#include <vector>
using namespace std;


vector<int>VectorConverter(string x){
    vector<int>out;
    for(int i = 0; i < x.length(); i++)
    {
        out.push_back(x[i]); 
    }
    return out;
}

void Encrypt(vector<int>&codeword, vector<int>&message){
    vector<int> values;
    for (int i = 0; i < codeword.size(); i++) {
        values.push_back(codeword[i] - 65);
    }
    int j = 1;
    bool capitalletters = true;
    for (int i = 0; i < message.size(); i++) {
        if ((message[i] >= 65 && message[i] <= 90) || (message[i] >= 97 && message[i] <= 122)) {
            if (j > codeword.size()) {
                j = 1;
            }
            if ((message[i] >= 97) && (message[i] <= 122)) {
                capitalletters = false;
                message[i] -= 32;
            }
            message[i] += values[j - 1];
            if (message[i] > 90) {
                message[i] -= 26;
            }
            if (capitalletters == false) {
                message[i] += 32;
                capitalletters = true;
            }
            cout << char(message[i]);
            j++;
        } 
        else{
            cout << char(message[i]);
        }
    }
}

void Decrypt(vector<int>&codeword, vector<int>&message) {
    vector<int> values;
    for (int i = 0; i < codeword.size(); i++) {
        values.push_back(codeword[i] - 65);
    }
    int count = 1;
    bool capitalletters = true;
    for (int i = 0; i < message.size(); i++) {
        if ((message[i] >= 65 && message[i] <= 90) || (message[i] >= 97 && message[i] <= 122)) {
            if (count > codeword.size()) {
                count = 1;
            }
            if ((message[i] >= 97) && (message[i] <= 122)) {
                capitalletters = false;
                message[i] -= 32;
            }
            message[i] -= values[count - 1];
            if (message[i] < 65) {
                message[i] += 26;
            }
            if (capitalletters == false) {
                message[i] += 32;
                capitalletters = true;
            }
            cout << char(message[i]);
            count++;
        } 
        else{
            cout << char(message[i]);
        }
    }
}

int main() {
    string type, codeword;
    cin >> type >> codeword;
    cin.ignore();
    string message,s;
    while (getline(cin, s)){
        message += s + '\n';
    }
    vector<int>vcodeword,vmessage;
    vcodeword=VectorConverter(codeword);
    vmessage=VectorConverter(message);
    if (type == "encrypt") {
        Encrypt(vcodeword, vmessage);
    } 
    else {
        Decrypt(vcodeword, vmessage);
    }
    return 0;
}