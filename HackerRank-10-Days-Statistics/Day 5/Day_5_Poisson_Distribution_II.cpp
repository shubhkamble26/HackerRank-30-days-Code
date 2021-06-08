#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<iomanip>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    float a,b;
    cin>>a>>b;
    
    double C_A= 160 + 40*(a+ a*a);
    double C_B= 128 + 40*(b+ b*b);
    cout<<fixed<<setprecision(3)<<C_A<<endl;
    cout<<fixed<<setprecision(3)<<C_B<<endl;
    return 0;
}