#!/usr/bin/env python3
import sys
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


def solve_(n,e,xyc):
    # your solution here
    xyc = [(x+3, y+3, c) for x,y,c in xyc]

    g = defaultdict(list)

    # x,y,0 if right and 1 if left

    mapp = defaultdict(int)
    for x,y,c in xyc:
        mapp[x,y] = c
        
    dp = [[[-10**18 for _ in range(2)] for _ in range(511)] for _ in range(511)]
    dp[510][0][0] = 0  # [y][x][right]
    for i in range(510,0,-1):

        dp[i][1][0]   = max(dp[i][1][0],   dp[i][1][1] - e)  # turn right
        dp[i][509][1] = max(dp[i][509][1], dp[i][509][0] - e)  # turn left

        for j in range(510):
            # move right
            dp[i][j+1][0] = max(dp[i][j+1][0], dp[i][j][0] + mapp[i,j])
            # move down
            dp[i-1][j][0] = max(dp[i-1][j][0], dp[i][j][0] + mapp[i,j])

        for j in range(510,0,-1):
            # move left
            dp[i][j-1][1] = max(dp[i][j-1][1], dp[i][j][1] + mapp[i,j])
            # move down
            dp[i-1][j][1] = max(dp[i-1][j][1], dp[i][j][1] + mapp[i,j])

    # log(dp[0])

    return max(max(x[0] for x in dp[1]), max(x[1] for x in dp[1]))


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    n,e = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    xyc = read_matrix(n)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n,e,xyc)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    # print(res)
