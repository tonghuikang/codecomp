import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(lst):  # fix inputs here
    lst = sorted(lst)
    console("----- solving ------")
    console(lst)

    if len(lst) > 40:
        return sum(lst) - len(lst)   

    base = 0
    minres = 10**11
    while base**len(lst) < (10**15):
        req = [base**i for i in range(len(lst))]
        diff = [abs(r-x) for r,x in zip(req, lst)]
        # console(req, base, diff, sum(diff))
        minres = min(minres, sum(diff))
        base += 1

    return minres


def console(*args):  # the judge will not read these print statement
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
# sys.stdin.readlines()

# for case_num in range(int(input())):
for _ in range(1):
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
    print(res)
