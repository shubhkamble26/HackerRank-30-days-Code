# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
a,b =sys.stdin.readlines()
num, den=list(map(int,a.strip().split())) 
n=int(b)
p_d=num/den

summation=0

for i in range(0,n):
    summation+=(1-p_d)**i * p_d
    
print(round(summation,3))
