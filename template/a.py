import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(N, op):  # fix inputs here
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
    # print("\n".join([str(x) for x in res]))
    # # return a string (i.e. not a list or matrix)
    # # return ""  


def console(*args):  # the judge will not read these print statement
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
# sys.stdin.readlines()

# for case_num in range(int(input())):
    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
k, nrows = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
grid = []
for _ in range(nrows):
    grid.append(int(input()))

res = solve(k, grid)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
print("\n".join([str(x) for x in res]))
