#!/usr/bin/env python3
import sys
# import getpass  # not available on codechef
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

m9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize
e18 = 10**18 + 10

# if testing locally, print to terminal with a different color
# OFFLINE_TEST = getpass.getuser() == "htong"
OFFLINE_TEST = False  # codechef does not allow getpass
def log(*args):
    if OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)

def solve(*args):
    # screen input
    if OFFLINE_TEST:
        log("----- solving ------")
        log(*args)
        log("----- ------- ------")
    return solve_(*args)

def read_matrix(rows):
    return [list(map(int,input().split())) for _ in range(rows)]

def read_strings(rows):
    return [input().strip() for _ in range(rows)]

def minus_one(arr):
    return [x-1 for x in arr]

def minus_one_matrix(mrr):
    return [[x-1 for x in row] for row in mrr]

# ---------------------------- template ends here ----------------------------


def solve_(n,m,mrr):
    # your solution here

    # just get 50% of the points here

    mrr.sort(key=lambda x:(x[1], -x[2]), reverse=True)

    cur = 10**6 + 100
    res = [cur]
    right = 0
    constrained = False
    increasing = True

    for i in range(1,n+1):
        # log(right, constrained, increasing)

        if constrained:
            # check feasibility, extend right
            while mrr and mrr[-1][1] < i:
                t,a,b = mrr.pop()
                if t == 0 and not increasing:
                    return [-1]
                if t == 1 and increasing:
                    return [-1]
                right = max(right, b)

        if right <= i:
            constrained = False

        if increasing:
            res.append(res[i-1] + 1)
        else:
            res.append(res[i-1] - 1)

        if mrr and mrr[-1][1] == i:
            t,a,b = mrr.pop()
            constrained = True
            increasing = t == 0
            right = b

    minres = min(res[1:]) - 1

    return [x - minres for x in res[1:]]


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    n,m = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(m)  # and return as a list of list of int
    mrr = minus_one_matrix(mrr)

    res = solve(n,m,mrr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)