#include <iostream>
#include <cmath>

using namespace std;

bool isPrime(int N){
	/*
	Complete the missing code here
	The function takes in an integer and returns true
	if it is prime. Otherwise, it returns false
	*/
	bool flag=true;
    for(int i = 2; i <= N / 2; i++) {
       if(N % i == 0) {
          flag = false;
          break;
       }
    }
    return flag;
	/*bool tf;
 	for (int i = 2; i < N; i++)
 	{
	 	if ((N % i) == 0)
	 	{
		 	tf = false;
		}
	 	else{
		 	tf = true;
	 	}
 	}
	return tf;*/
}

bool isTwinPrime(int N){
	/*
	Complete the missing code. The function takes in 
	an integer and returns true if it is a twin prime.
	Otherwise, it returns false. The function should
	make use of the isPrime() function in some way
	*/
	bool tf;
    int twinAdd = N+2;
    int twinMinus = N-2;
	if(isPrime(N)){
		if(isPrime(twinAdd) && isPrime(twinMinus)){
			tf = false;
		}
		else{
			tf = true;
		}
	}
	return tf;
}

int main(){
	int N;
	cin >> N;
	for (int i = 0; i < N; ++i){
		int p;
		cin >> p;
		if (isTwinPrime(p)){
			cout << "true" << endl;
		}
		else{
			cout << "false" << endl;
		}
	}
	return 0;
}
