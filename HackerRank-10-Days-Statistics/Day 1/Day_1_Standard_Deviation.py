#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    n=len(arr)
    mean=sum(arr)/n
    summation=0
    for i in arr:
        summation+=(i-mean)**2
        
    print(round((summation/n)**0.5,1))
        

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
