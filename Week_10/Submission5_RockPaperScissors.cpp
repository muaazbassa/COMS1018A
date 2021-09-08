//Mu'aaz Bassa
//Submission 5: Rock-Paper-Scissors
#include <iostream>
using namespace std;

int main() {
    string sPlayer1,sPlayer2;
    int iPlayer1=0;
    int iPlayer2=0;
    cin >> sPlayer1;
    cin >> sPlayer2;
//Player 1
    if (sPlayer1=="rock")
    {
        iPlayer1=0;
        //cout<<"P1-0";
    }
    else if (sPlayer1=="scissors")
    {
        iPlayer1=1;
        //cout<<"P1-1";
    }
    else if (sPlayer1=="paper")
    {
        iPlayer1=2;
        //cout<<"P1-2";
    }
//Player 2  
    if (sPlayer2=="rock")
    {
        iPlayer2=0;
       // cout<<"P2-0";
    }
    else if (sPlayer2=="scissors")
    {
        iPlayer2=1;
        //cout<<"P2-1";
    }
    else if (sPlayer2=="paper")
    {
        iPlayer2=2;
        //cout<<"P2-2";
    }
//Results
    if ((iPlayer1==0)&&(iPlayer2==2))
    {
        cout<<"Player 2 wins";
    }
    else if ((iPlayer1==1)&&(iPlayer2==0))
    {
        cout<<"Player 2 wins";
    }
    else if ((iPlayer1==2)&&(iPlayer2==1))
    {
        cout<<"Player 2 wins";
    }
    else if (iPlayer1==iPlayer2)
    {
        cout<<"Tie";
    }
    else
    {
        cout<<"Player 1 wins";
    }
    
    return 0;
}