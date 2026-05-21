#include <stdio.h>
#include <iostream>
#include <math.h>
#include <cmath>
#include <vector>
using namespace std;

int main()
{

    int n;
    int altura;
    int distancia;
    int resultat;
    
    cin >> n;
    
    for (int i = 0;i < n;i++){
        cin >> altura;
        cin >> distancia;
        resultat = sqrt(altura*altura+distancia*distancia);
        cout << resultat << endl;
      
      }
}
