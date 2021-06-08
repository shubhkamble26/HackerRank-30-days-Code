#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<iomanip>
#include<bits/stdc++.h>
using namespace std;

double cum_dist(double x,double mean, double dev){
    double dist =0.5*(1+ erf((x-mean)/(sqrt(2)*dev))) ;
    return dist;
}


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    double mean, dev, val, lower_bound, upper_bound;
    cin>>mean>>dev>>val>>lower_bound>>upper_bound;
    
    cout<<fixed<<setprecision(3)<<cum_dist(val,mean,dev)<<endl;
    cout<<fixed<<setprecision(3)<<(cum_dist(upper_bound,mean,dev)-cum_dist(lower_bound,mean,dev))<<endl;
    //ed)<<normal_dist(upper_bound,mean,dev)-normal_dist(lower_bound,mean,dev)<<endl;
    
       
    return 0;
}
