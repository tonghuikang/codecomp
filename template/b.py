import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(lst):  # fix inputs here
    console("----- solving ------")

    taken = [False for _ in lst]
    res = [-1 for _ in lst]

    maxidx = lst.index(max(lst))
    res[0] = lst[maxidx]
    taken[maxidx] = True
    pergcd = lst[maxidx]

    console(taken)

    for i,_ in enumerate(lst[1:], start=1):
        curmax = -1
        idx = -1
        for j,y in enumerate(lst):
            if taken[j]:
                continue
            val = math.gcd(pergcd,y)
            if val > curmax:
                curmax = val
                idx = j

        pergcd = curmax
        res[i] = lst[idx]
        taken[idx] = True

    # return a string (i.e. not a list or matrix)
    return res


def console(*args):  # the judge will not read these print statement
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
# sys.stdin.readlines()

for case_num in range(int(input())):
    # read line as a string
    # strr = input()

    # read line as an integer
    _ = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    lst = list(map(int,input().split()))

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
    print(" ".join(str(x) for x in res))
