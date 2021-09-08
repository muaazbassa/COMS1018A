//The First Task
#include <iostream>
#include <string>
using namespace std;

void ASCII(string letter)
{
    for (int i = 0; i < letter.length(); i++)
    {
        char x = letter.at(i);
        cout << int(x) - 65 << " ";
    }
}

int main() {
    string x;
    cin >> x;
    ASCII(x);
    return 0;
}
