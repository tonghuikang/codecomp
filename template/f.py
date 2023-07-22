#!/usr/bin/env python3
import sys
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

m9 = 998244353
yes, no = "YES", "NO"
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize
e18 = 10**18 + 10

# if testing locally, print to terminal with a different color
OFFLINE_TEST = False
CHECK_OFFLINE_TEST = True
# CHECK_OFFLINE_TEST = False  # uncomment this on Codechef
if CHECK_OFFLINE_TEST:
    import getpass
    OFFLINE_TEST = getpass.getuser() == "htong"

def log(*args):
    if CHECK_OFFLINE_TEST and OFFLINE_TEST:
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


def solve_(n,m,srr):
    # your solution here
    mrr = [[1 for _ in range(m+1)] for _ in range(n+1)]

    for i,row in enumerate(srr):
        for j,cell in enumerate(row):
            if cell == ".":
                mrr[~i][~j] = 0

    # for row in mrr:
    #     log(row)

    dp00 = [[0 for _ in range(m+1)] for _ in range(n+1)]
    dp11 = [[0 for _ in range(m+1)] for _ in range(n+1)]
    dp10 = [[0 for _ in range(m+1)] for _ in range(n+1)]
    dp01 = [[0 for _ in range(m+1)] for _ in range(n+1)]

    j = 0
    for i in range(n+1):
        dp11[i][j] = 1
        # dp10[i][j] = 1
        # dp01[i][j] = 1
        # dp00[i][j] = 1
        
    i = 0
    for j in range(m+1):
        dp11[i][j] = 1
        # dp10[i][j] = 1
        # dp01[i][j] = 1
        # dp00[i][j] = 1


    for i in range(1,n+1):
        for j in range(1,m+1):
            # log()
            # log(dp00)
            # log(dp01)
            # log(dp10)
            # log(dp11)

            # xx
            # *x

            dp11[i][j] += dp11[i-1][j] * (dp01[i][j-1] + dp11[i][j-1])
            dp01[i][j] += dp11[i-1][j] * (dp00[i][j-1] + dp10[i][j-1])

            dp11[i][j] = dp11[i][j]%998244353
            dp01[i][j] = dp01[i][j]%998244353

            if mrr[i][j] == 1:
                continue

            # xx
            # *o

            dp10[i][j] += dp11[i-1][j] * (dp01[i][j-1] + dp11[i][j-1])
            dp00[i][j] += dp11[i-1][j] * (dp00[i][j-1] + dp10[i][j-1])

            # oo
            # *o

            # dp10[i][j] += dp00[i-1][j] * (dp01[i][j-1] + dp11[i][j-1])
            dp00[i][j] += dp00[i-1][j] * (dp00[i][j-1] + dp10[i][j-1])

            # xo
            # *o

            dp10[i][j] += dp10[i-1][j] * (dp01[i][j-1] + dp11[i][j-1])
            dp00[i][j] += dp10[i-1][j] * (dp00[i][j-1] + dp10[i][j-1])

            # ox
            # *o

            # dp10[i][j] += dp01[i-1][j] * (dp01[i][j-1] + dp11[i][j-1])
            dp00[i][j] += dp01[i-1][j] * (dp00[i][j-1] + dp10[i][j-1])

            dp10[i][j] = dp10[i][j]%998244353
            dp00[i][j] = dp00[i][j]%998244353

    # log()
    # log(dp00)
    # log(dp01)
    # log(dp10)
    # log(dp11)

    return (dp00[-1][-1] + dp01[-1][-1] + dp10[-1][-1] + dp11[-1][-1])%m9


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    # n = int(input())
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
    mrr = read_strings(n)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n,m,mrr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
