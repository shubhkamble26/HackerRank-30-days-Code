#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<bits/stdc++.h>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    float num, den;
    int n;
    cin>>num>>den>>n;
    float p_d=num/den;
    
    cout<<fixed<<setprecision(3)<<pow(1-p_d,n-1)*p_d<<endl; 
    return 0;
}
