# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys

n_tickets, n_students, mean, dev = map(float, sys.stdin.readlines())

new_mean = mean*n_students
new_dev = dev * n_students**0.5

prob=0.5*(1+math.erf((n_tickets - new_mean)/(math.sqrt(2)*new_dev)))
print(round(prob,4))