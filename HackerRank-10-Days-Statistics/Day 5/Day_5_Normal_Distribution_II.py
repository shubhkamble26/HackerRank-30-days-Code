# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys

a,b,c = sys.stdin.readlines()
mean, dev = list(map(int,a.strip().split()))
std_marks80=int(b)
std_marks60=int(c)

def cum_dist(x):
    dist=0.5*(1+ math.erf((x-mean)/(dev*math.sqrt(2))))
    return dist

print(round((1-cum_dist(std_marks80))*100,2))
print(round((1-cum_dist(std_marks60))*100,2))
print(round(cum_dist(std_marks60)*100,2))
