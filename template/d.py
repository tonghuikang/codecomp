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

m9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize
e18 = 10**18 + 10

# if testing locally, print to terminal with a different color
OFFLINE_TEST = getpass.getuser() == "htong"
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


def solve_(mrr, c):
    # am I understanding this wrongly?

    # your solution here

    def solve_segment(pos0, pos1):
        pos0.sort()
        pos1.sort()
        # log(pos0)
        # log(pos1)
        if not mrr:
            return 0

        a = len(pos0)
        b = len(pos1)

        LARGE = 10**18
        dp = [[LARGE for _ in range(b+5)] for _ in range(a+5)]
        dp[0][0] = 0

        for i in range(5):
            pos0.append(10**16)
            pos1.append(10**16)

        # log(dp)

        for i in range(a+1):
            for j in range(b+1):
                # log(i,j,a,b,dp[i+1])
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 2*(pos0[i+1-1]))
                dp[i+2][j] = min(dp[i+2][j], dp[i][j] + 2*(pos0[i+2-1]) + c)

                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 2*(pos1[j+1-1]))
                dp[i][j+2] = min(dp[i][j+2], dp[i][j] + 2*(pos1[j+2-1]) + c)

                dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j] + 2*max(pos0[i+1-1], pos1[j+1-1]))

        # log(dp[a][b])
        return dp[a][b]

    pos0_pos = []
    pos1_pos = []

    pos0_neg = []
    pos1_neg = []

    for a,b in mrr:

        if a > 0:
            if b == 0:
                pos0_pos.append(a)
            else:
                pos1_pos.append(a)

        if a < 0:
            if b == 0:
                pos0_neg.append(-a)
            else:
                pos1_neg.append(-a)
        

    return solve_segment(pos0_pos, pos1_pos) + solve_segment(pos0_neg, pos1_neg)


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
    n,c = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(n)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(mrr,c)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    # print(res)
