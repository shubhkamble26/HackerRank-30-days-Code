#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<bits/stdc++.h>
using namespace std;


int factorial(int n){
    if(n==0 || n==1)
        return 1;
    return n*factorial(n-1);
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    float a,b;
    float summation;
    cin>>a>>b;
    float p_b=a/(a+b);
    //float p_g=b/(a+b);
 
    
    for(int j=3;j<=6;j++){
        int n_c_r = factorial(6)/(factorial(j)*factorial(6-j));
        double powers =  pow(p_b,j)*pow(1-p_b,6-j);
        summation+= n_c_r * powers;
    }
    
    cout<<fixed<<setprecision(3)<<summation<<endl;
    //fixed<<setprecision(3)
     
    return 0;
}
