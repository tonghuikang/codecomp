import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(strr, k):  # fix inputs here
    console("----- solving ------")
    console(strr, k)

    arr = [int(x) for x in strr]
    res = [1 for _ in strr]

    for i,a in enumerate(arr):
        if a == 0:
            if i-k >= 0:
                res[i-k] = 0
            if i+k < len(arr):
                res[i+k] = 0
    
    for i,a in enumerate(arr):
        if a == 1:                
            if i-k >= 0 and i+k < len(arr):
                if res[i-k] == 0 and res[i+k] == 0:
                    return -1

            elif i-k >= 0:
                if res[i-k] == 0:
                    return -1

            elif i+k < len(arr):
                if res[i+k] == 0:
                    return -1

            else:  # not(i-k >= 0) and not(i+k < len(arr)):
                return -1

    return "".join(str(x) for x in res)


def console(*args):  # the judge will not read these print statement
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
# sys.stdin.readlines()

for case_num in range(int(input())):
    # read line as a string
    strr = input()

    # read line as an integer
    k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    # lst = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(strr, k)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
