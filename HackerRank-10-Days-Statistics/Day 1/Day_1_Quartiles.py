#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def median(arr):
    n=len(arr)
    mid=n//2
    if(n%2==1):
        median=arr[mid]
    else:
        median=(arr[mid-1]+arr[mid])//2
    return median
    

def quartiles(arr):
    # Write your code here
    n=len(arr)
    s_arr=sorted(arr)
    
    #mid=n//2
    Q2=median(s_arr)
    
    arr_1=s_arr[:n//2]
    arr_2=s_arr[(n+1)//2:]
    Q1=median(arr_1)
    Q3=median(arr_2)
    
    Quartiles=[Q1,Q2,Q3]
        
    return Quartiles

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
