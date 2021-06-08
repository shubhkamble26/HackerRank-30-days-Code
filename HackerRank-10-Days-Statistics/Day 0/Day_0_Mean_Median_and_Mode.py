# Enter your code here. Read input from STDIN. Print output to STDOUT
num_of_elements=int(input())
lst=list(map(int,input().split()))

#Mean
mean= sum(lst)/num_of_elements
print(mean)

#Median
if(num_of_elements%2==1):
    median=sorted(lst)[int(num_of_elements/2)]
else:
    median=(sorted(lst)[int(num_of_elements/2) - 1]+sorted(lst)[int(num_of_elements/2)])/2
print(median)

#mode
from scipy import stats
mde=int(stats.mode(lst)[0])
print(mde)