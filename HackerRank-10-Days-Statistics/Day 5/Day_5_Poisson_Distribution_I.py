# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys
a,b = sys.stdin.readlines()
lamda = float(a)
k=int(b)

def factorial(n):
    if (n==0 or n==1):
        return 1
    return n*factorial(n-1)

print(round((lamda**k * math.exp(-lamda))/factorial(k),3))

