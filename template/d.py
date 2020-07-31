#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

#
# Complete the 'countCups' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY balls
#  3. 2D_INTEGER_ARRAY swaps
#  4. 2D_INTEGER_ARRAY queries
#

def countCups(n, balls, swaps, queries):
    balls = set(balls)
    
    for a,b in swaps:
        x = a in balls
        y = b in balls
        
        if x and y:
            continue
        if (not x) and (not y):
            continue
        if x and (not y):
            balls.remove(a)
            balls.add(b)
        if (not x) and y:
            balls.add(a)
            balls.remove(b)
            
    balls = sorted(balls)
    
    res = []
    for a,b in queries:
        x = bisect.bisect_left(balls, a)
        y = bisect.bisect_right(balls, b)
        res.append(y-x)
    
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    s = int(first_multiple_input[2])

    q = int(first_multiple_input[3])

    balls = list(map(int, input().rstrip().split()))

    swaps = []

    for _ in range(s):
        swaps.append(list(map(int, input().rstrip().split())))

    query = []

    for _ in range(q):
        query.append(list(map(int, input().rstrip().split())))

    result = countCups(n, balls, swaps, query)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
