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

def solve(lst):  # fix inputs here
    # console("----- solving ------")

    # console(lst)

    d = defaultdict(list)
    res = 0

    for i,x in enumerate(lst):
        d[x].append(i)

    # console(d)

    idxs = d.values()

    for k1,v1 in enumerate(idxs):
        if len(v1) == 1:
            continue

        for k2,v2 in enumerate(idxs):
            if len(v2) == 1:
                continue 

            if k1 == k2:
                continue

            j = 0
            cnt = 0
            segments = [0 for _ in v1]
            for i,x in enumerate(v1):  # reference
                while j < len(v2) and v2[j] < x:
                    j += 1
                    cnt += 1
                segments[i] = cnt

            psum = segments
            # csum = 0
            # for x in segments:
            #     csum += x
            #     psum.append(csum)

            for i in range(len(psum)):
                for j in range(i+1, len(psum)):
                    res += psum[i] * (psum[j] - psum[i])

    for v in idxs:
        if len(v) >= 4:
            res += ncr(len(v), 4)
            # lst.append(len(v2) - cnt)

    
    # return a string (i.e. not a list or matrix)
    return res


def console(*args):  # the judge will not read these print statement
    # print('\033[36m', *args, '\033[0m', file=sys.stderr)
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
