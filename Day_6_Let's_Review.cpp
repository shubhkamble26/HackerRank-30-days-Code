#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int n;
    cin>>n;
    string st[n];
    for(int i=0;i<n;i++){
        cin>>st[i];
    }  
    for(auto i : st){
        for(int j=0;j<i.size();j+=2){
            cout<<i[j];
        }
        cout<<" ";
        for(int k=1;k<i.size();k+=2){
            cout<<i[k];
            }   
    cout<<endl;
    }
    
    return 0;
}