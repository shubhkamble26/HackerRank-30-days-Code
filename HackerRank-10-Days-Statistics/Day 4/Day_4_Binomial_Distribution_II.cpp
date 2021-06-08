#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int factorial(int n){
    if(n==1 ||  n==0)
        return 1;
    return n*factorial(n-1);
}


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int a,b;
    float p_r=float(a/100);
    cin>>a>>b;
    float sum1, sum2;
    
    for (int i=0;i<=2;i++){
        int n_c_r=factorial(b)/(factorial(b-i)*factorial(i));
        float powers=pow(p_r,i)*pow(1-p_r,10-i);

        sum1+=n_c_r*powers;
    }
    
    for (int j=2;j<=b;j++){
        int n_c_r=factorial(b)/(factorial(10-j)*factorial(j));
        float powers=pow(p_r,j)*pow(1-p_r,b-j);

        sum2+=n_c_r*powers;
    }
    
    cout<<sum1<<endl;
    cout<<sum2<<endl;
    
    
    return 0;
}
