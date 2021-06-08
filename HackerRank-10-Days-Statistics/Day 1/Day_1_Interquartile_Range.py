#!/bin/python3

import math
import os
import random
import re
import sys
from statistics import median

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def median():
    

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    n=len(freqs)
    lst=[]
    for i in range(n):
        for j in range(freqs[i]):
            lst.append(values[i])
                    
    s_arr=sorted(lst)
    
                    
            

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
