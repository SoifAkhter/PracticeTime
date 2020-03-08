#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    pass

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    lst = [0]*(n+1)

    for _ in range(m):
        i,e,s = (map(int, input().rstrip().split()))
        lst[i-1] += s
        if e<=len(lst):
            lst[e] -= s
    max=x=0
    for i in lst:
         x += i
         if max < x:
            max=x


    result = max

    fptr.write(str(result) + '\n')

    fptr.close()
