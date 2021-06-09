#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    s=''
    
    for i in range(len(sentence)):
        if(sentence[i].islower()):
            s+=sentence[i].upper()
        elif(sentence[i].isupper()):
                s+=sentence[i].lower()
        else:
            s+=sentence[i]
            
    s2=s.split(' ')
    lst=[]
    for i in range(len(s2)):
        lst.append(s2[len(s2)-i-1])

    return " ".join(lst)
        

            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = reverse_words_order_and_swap_cases(sentence)

    fptr.write(result + '\n')

    fptr.close()
