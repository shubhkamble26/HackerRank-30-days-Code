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
    float lambda;
    int k;
    cin>>lambda>>k;
    
    double p=pow(lambda,k)*exp(-lambda)/factorial(k);
    cout<<fixed<<setprecision(3)<<p<<endl;  
    return 0;
}
