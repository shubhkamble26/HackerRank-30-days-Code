# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
[a,b]=sys.stdin.readlines()
num, den=map(int,a.strip().split())
n=int(b)

p_d=num/den
print(round((((1-p_d)**(n-1)) * p_d),3))
