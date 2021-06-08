# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys

a,b,c = sys.stdin.readlines()
mean, dev = list(map(float,a.strip().split()))
val=float(b)
lowr_bound,uppr_bound=list(map(float,c.strip().split()))

def cum_dist(x):
    dist=0.5*(1+ math.erf((x-mean)/(dev*math.sqrt(2))))
    return dist

print(round(cum_dist(val),3))
print(round(cum_dist(uppr_bound)-cum_dist(lowr_bound),3))