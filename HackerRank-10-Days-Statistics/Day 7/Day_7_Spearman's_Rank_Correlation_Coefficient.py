# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys
n, X, Y = sys.stdin.readlines()
n=int(n)
X=list(map(float,X.strip().split()))
Y=list(map(float,Y.strip().split()))
x_sort=sorted(X)
y_sort=sorted(Y)

rank_x=[0]*10
rank_y=[0]*10
r=1

for i in x_sort:
    for j in X:
        if i==j:
            rank_x[X.index(j)] = r
            r+=1

r=1
for i in y_sort:
    for j in Y:
        if i==j:
            rank_y[Y.index(j)] = r
            r+=1
            
d_i2=sum([(rank_x[i]-rank_y[i])**2 for i in range(n)])

r_s=1-6*(d_i2/(n*(n**2-1)))
print(round(r_s,3))
