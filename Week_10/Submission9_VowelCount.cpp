//Mu'aaz Bassa
//Submission 9: Vowel Count

#include <iostream>
using namespace std;

int main() {
    string sInput;
    int iVowel;
    getline(cin, sInput);
    while (sInput != "end") {
        iVowel = 0;
        for (int i = 0; i < sInput.length(); i++) {
            if ((sInput[i] == 'a') || (sInput[i] == 'e') || (sInput[i] == 'i') ||
                (sInput[i] == 'o') || (sInput[i] == 'u') || (sInput[i] == 'A') ||
                (sInput[i] == 'E') || (sInput[i] == 'I') || (sInput[i] == 'O') ||
                (sInput[i] == 'U')) {
                iVowel = iVowel + 1;
            }
        }
        getline(cin, sInput);
        cout << iVowel << endl;
    }
    return 0;
}