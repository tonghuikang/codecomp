#!/usr/bin/env python3
import sys
import getpass  # not available on codechef
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

M9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize

# if testing locally, print to terminal with a different color
OFFLINE_TEST = getpass.getuser() == "hkmac"
# OFFLINE_TEST = False  # codechef does not allow getpass
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


def solve_(mrr, h, w):
    if h == w == 1:
        return "Draw"
    
    # your solution here
    # mrr = [[cell if (i+j)%2 == 0 else -cell for i,cell in enumerate(row)] for j,row in enumerate(mrr)]
    # log(mrr)

    dp = [[0 for _ in range(w)] for _ in range(h)]
    if (h+w-2)%2:
        dp[0][0] = -mrr[0][0]
    else:
        dp[0][0] = mrr[0][0]

    for i in range(w-2,-1,-1):
        if (i+h-1)%2:
            dp[0][i] = dp[-1][i+1] - mrr[-1][i]
        else:
            dp[0][i] = dp[-1][i+1] + mrr[-1][i]

    for i in range(h-2,-1,-1):
        if (i+w-1)%2:
            dp[i][-1] = dp[i+1][-1] - mrr[i][-1]
        else:
            dp[i][-1] = dp[i+1][-1] + mrr[i][-1]
    
    for i in range(1,h):
        for j in range(1,w):
            if (i+j)%2:
                dp[i][j] = min(dp[i][j-1], dp[i-1][j]) - mrr[i][j]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j]) + mrr[i][j]


    dp[-1][-1] -= mrr[-1][-1]
    log("dp")
    log(dp)

    if dp[-1][-1] == 0:
        return "Draw"

    if (i+j)%2 == 1:
        if dp[-1][-1] >= 0:
            return "Takahashi"
        return "Aoki"
    
    if dp[-1][-1] >= 0:
        return "Aoki"
    return "Takahashi"


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    h,w = list(map(int,input().split()))
    # lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    mrr = read_strings(h)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)
    mrr = [[1 if cell == "+" else -1 for cell in row] for row in mrr]

    res = solve(mrr,h,w)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)