# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys
max_wt, n, mean_wt, dev = map(int, sys.stdin.readlines())

new_mean = mean_wt * n
new_dev = dev * (n**0.5)

p=0.5 * (1+ math.erf((max_wt-new_mean)/(math.sqrt(2)*new_dev)))
print(round(p,4))
