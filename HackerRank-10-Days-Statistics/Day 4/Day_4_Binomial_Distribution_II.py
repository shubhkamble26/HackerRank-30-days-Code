# Enter your code here. Read input from STDIN. Print output to STDOUT
a,b=list(map(int,input().strip().split()))

p_r=a/100

def factorial(n):
    if(n==0 or n==1):
        return 1
    return n*factorial(n-1)

summation1=0
summation2=0

for i in range(3):
    n_C_r=factorial(b)/(factorial(i)*factorial(b-i))
    powers=(p_r**i)*((1-p_r)**(b-i))
    summation1+=n_C_r*powers
    
for i in range(2,b+1):
    n_C_r=factorial(b)/(factorial(i)*factorial(b-i))
    powers=(p_r**i)*((1-p_r)**(b-i))
    summation2+=n_C_r*powers
    
print(round(summation1,3))
print(round(summation2,3))
