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
    float sum=0;
    
    for(int i=0;i<n;i++){
        sum+=pow(1-p_d,i)*p_d;
    }  
    cout<<fixed<<setprecision(3)<<sum<<endl;
    return 0;
}