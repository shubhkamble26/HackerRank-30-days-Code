#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<iomanip>
using namespace std;

double cum_dist(double x, double mean, double dev){
    double dist=0.5*(1+erf((x-mean)/(sqrt(2)*dev)));
    return dist;
}


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    double mean, dev, std_marks80, std_marks60;
    cin>>mean>>dev>>std_marks80>>std_marks60;
    
    cout<<fixed<<setprecision(2)<<(1-cum_dist(std_marks80,mean,dev))*100<<endl;
    cout<<fixed<<setprecision(2)<<(1-cum_dist(std_marks60,mean,dev))*100<<endl;
    cout<<fixed<<setprecision(2)<<(cum_dist(std_marks60,mean,dev))*100<<endl;
    return 0;
}
