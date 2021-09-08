//Mu'aaz Bassa
//Submission 1: Marks
#include <iostream>
#include <vector>

using namespace std;

void Order(vector <string> &students, vector <int> &grades,int &N){
    for (int j = 0; j < N; ++j){
        for (int k = j+1; k < N; ++k){
            if (students[j] > students[k]){
                swap(students[j], students[k]);
                swap(grades[j], grades[k]);
            }
        }
    }
}

int main() {
    
    int N;
    cin>>N;
    vector <string> students;
    vector <int> grades;
    string name;
    int mark;

    for (int i=0; i<N;i++){
        cin >> name>>mark;
        students.push_back(name);
        grades.push_back(mark);
    }
    Order(students,grades,N);
    
    for (int i = 0; i < N; ++i){
        cout << students[i] << ": " << grades[i] << endl;
    }

    return 0;
}