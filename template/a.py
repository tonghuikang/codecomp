#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'performOperations' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER_ARRAY op
#

def performOperations(N, op):  # fix inputs here
    # console("----- solving ------")
    # console(k, arr)
    k = N
    arr = op

    summ = (k*(k+1))//2

    const = summ - 1 - k

    first_val = 1
    last_val = k

    res = []

    for a in arr:
        if 1 < a < k or a == first_val or a == last_val:
            first_val, last_val = last_val, first_val
            res.append(const + first_val + last_val)
            continue
        last_val = a
        res.append(const + first_val + last_val)
    
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N, M = list(map(int, input().rstrip().split()))
    
    op = []
    for i in range(M):
        op.append(int(input().rstrip()))

    result = performOperations(N, op)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()