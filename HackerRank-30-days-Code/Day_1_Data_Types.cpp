#include <iostream>
#include <iomanip>
#include <limits>

using namespace std;

int main() {
    int i = 4;
    double d = 4.0;
    string s = "HackerRank ";

    
    // Declare second integer, double, and String variables.
    int i1;
    double d1;
    string s1{};
    
    
    // Read and save an integer, double, and String to your variables.
    cin>>i1>>d1;//>>s1;
    cin.ignore();
    getline(cin,s1);
    // Note: If you have trouble reading the entire string, please go back and review the Tutorial closely.
    
    // Print the sum of both integer variables on a new line.
    cout<<i+i1<<endl;
    
    // Print the sum of the double variables on a new line.
    cout<<fixed<<setprecision(1)<<d+d1<<endl;
    // Concatenate and print the String variables on a new line
    cout<<s + s1<<endl;
    // The 's' variable above should be printed first.

    return 0;
}