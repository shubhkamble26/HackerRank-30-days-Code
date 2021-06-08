# Enter your code here. Read input from STDIN. Print output to STDOUT
a,b=list(map(float,input().strip().split()))

p_b=a/(a+b)

def factorial(n):
    if(n==0 or n==1):
        return 1
    return n*factorial(n-1)

summation=0

for i in range(3,7):
    n_C_r=factorial(6)/(factorial(i)*factorial(6-i))
    powers=(p_b**i)*((1-p_b)**(6-i))
    summation+=n_C_r*powers
    
print(round(summation,3))