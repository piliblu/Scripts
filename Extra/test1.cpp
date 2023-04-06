//
//  main.cpp
//  Tarea4
//
//  Created by Maria Guadalupe on 4/5/21.
//

#include <iostream>
using namespace std;

int main() {
    int n1, n2, n3 ; // n1 es el numero ingresado, n2 es el segundo digito, n3 es el primer digito
    cout << "Entre el numero: ";
    cin >> n1;
    
    if(n1 <= 99 && n1 > 9){ // el numero es de 2 digitos
        if ( n1 % 2 == 0)
            cout << n1 << " es par. ";
        else
            cout << n1 << " es impar. ";
        n2=n1%10;
        n3=n1/10%10;
        cout <<" Los digitos son: " << n3 << " y " << n2 << ". ";
        if ( n3 % 2 == 0)
            cout << n3 << " es par. ";
        else
            cout << n3 << " es impar. ";
        if ( n2 % 2 == 0)
            cout << n2 << " es par. ";
        else
            cout << n2 << " es impar. ";}
        
    else // el numero no cumple con la condicion de ser de 2 digitos.
        cout << "Numero incorrecto, por favor ingrese un valor de 2 digitos. ";
return 0;
}
