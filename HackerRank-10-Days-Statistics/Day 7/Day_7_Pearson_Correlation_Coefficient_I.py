# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys
n, X, Y = sys.stdin.readlines()

n=int(n)
X=list(map(float,X.strip().split()))
Y=list(map(float,Y.strip().split()))

mean_X=sum(X)/n
var_X=0
mean_Y=sum(Y)/n
var_Y=0

for i in X:
    var_X+=((i-mean_X)**2)/n
    
for j in Y:
    var_Y+=((j-mean_Y)**2)/n

cov=0

for i in range(n):
    cov+=(X[i]-mean_X)*(Y[i]-mean_Y)/n
    
pearson_corr_coef=cov/(math.sqrt(var_X)*math.sqrt(var_Y))

print(round(pearson_corr_coef,3))