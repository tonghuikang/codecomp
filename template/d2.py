import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy

import operator as op
from functools import reduce


@functools.lru_cache(maxsize=None)
def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom  # or / in Python 2

for i in range(3000):
    ncr(i, 4)

def solve(arr):  # fix inputs here
    console("----- solving ------")
    console(arr)

    n = len(arr)
    # console(lst)

    l = [0] * (n+1)
    ans = 0
 
    for j in range(n):
        r = [0] * (n+1)
        for k in range(n-1,j,-1):
            ans += l[arr[k]] * r[arr[j]]
            r[arr[k]] += 1
        l[arr[j]] += 1
        
        console(r)
        console(l)
        console(ans)

    
    # return a string (i.e. not a list or matrix)
    return ans


def console(*args):  # the judge will not read these print statement
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
inp = sys.stdin.readlines()

for case_num in range(int(inp[0])):
    # read line as a string
    # strr = input()

    # read line as an integer
    # _ = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    lst = list(map(int,inp[2*case_num+2].split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(lst)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
