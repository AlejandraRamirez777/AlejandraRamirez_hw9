#include <iostream>
#include <ctime>

using namespace std;

//Declara funciones
int fibonacci(int N);
float get_time(int N);

int main(){
    //ciclo para imprimir primeros 35 valores de N con el tiempo se tardo
    for( int a = 0; a < 35; a = a + 1 ) {
      //cout << a << "," << get_time(a) << "," <<  fibonacci(a) << endl;
      cout << a << "," << get_time(a) << endl;
   }

   return 0;
}

//funcion fibonacci
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

//funcion tiempo que tardo
float get_time(int N){
    clock_t t;
    t = clock();
    fibonacci(N);
    t = clock() - t;
    float time = ((float)t)/CLOCKS_PER_SEC;
return time;
}
