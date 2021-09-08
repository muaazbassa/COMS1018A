//Mu'aaz Bassa
//Submission 4: Dynamic Matrix
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int Row,Col;
    cin>>Row; // num of rows
    cin>>Col; // num of cols in each row
    auto default_value = 0; // default value of all int elements
    vector<vector<int>> matrix(Row, vector<int>(Col, default_value));
    int NoInput,RowIn,ColIn,NewValue;
    cin>>NoInput;
    for (size_t i = 0; i < NoInput; i++)
    {
        cin>>RowIn;
        cin>>ColIn;
        cin>>NewValue;
        matrix[RowIn][ColIn]=NewValue;
    }
    for (int i = 0; i < matrix.size(); i++)
    {
        for (int j = 0; j < matrix[i].size(); j++)
        {
            cout << matrix[i][j] << " ";
        }   
        cout << endl;
    }
    return 0;
}