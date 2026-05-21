#include <stdio.h>
#include <iostream>
#include <math.h>
#include <cmath>
#include <vector>
using namespace std;

int main()
{

   int n;

   cin >> n;
  for (int i = 0;i < n;i++){

    int a; //nombre de casos, mida llista
    int max = -(10*10*10*10*10*10) -1; //on posarem el maxim
    int sum = 0; //vegades que surt el maxim
    
    cin >> a;   //llegim el nombre de vegades A

    vector<long long int> v(a);//on posam els nombres participants
    
    //legim totes les dades:

    for (int y = 0;y < a;y++){
        cin >> v[y];
    }
    for (int y = 0;y < a;y++){
        //hem de veure si hi ha un nou maxim
        if(max < v[y]){
            max = v[y];
            }
        //hem de veure si es igual al maxim i sumar un nombre a sum
        if ( v[y] == max){
            sum++;
            }
    }
    cout << max << " " << sum << endl;
  }
}
