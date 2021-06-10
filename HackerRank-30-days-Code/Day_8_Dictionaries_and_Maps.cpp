#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
#include<string>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
     int n;
     cin>>n;
     string name;
     map<string, int> phone_no;
     for (int i=0;i<n;i++){
         cin>>name;
         cin>>phone_no[name];
     }
     
     while(cin>>name){
         if(phone_no.find(name)!=phone_no.end()){
            cout<<name<<"="<<phone_no.find(name)->second<<endl;
         }
         else{
             cout<<"Not found"<<endl;
         }
     }
     
    return 0;
}
