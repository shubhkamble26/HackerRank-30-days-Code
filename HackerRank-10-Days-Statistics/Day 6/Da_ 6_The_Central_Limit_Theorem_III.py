# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys
sample_size, mean, dev, perc, z = map(float,sys.stdin.readlines())

A=(mean - z*dev/math.sqrt(sample_size))
B=(mean + z*dev/math.sqrt(sample_size))

print(round(A,2))
print(round(B,2))
