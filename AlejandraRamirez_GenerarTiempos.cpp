#include <iostream>

using namespace std;
int fibonacci(int N);
int get_time();

int main(){


   return 0;
}

int fibonacci( int N ) {
    int sol;
   //Caso base, se retorna N si es menor o igual a 1
    if (N <= 1)
	sol = N;
    //De lo contrario, se ejecuta la operacion siguiente
    else
	sol = (fibonacci(N-1) + fibonacci(N-2));
    
    return sol;
}
