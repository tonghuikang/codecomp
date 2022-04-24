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

LARGE = 10**18

def solve_(arr, d):
    # your solution here

    def dist(a,b):
        # https://math.stackexchange.com/questions/1951658/calculate-distance-between-two-values-in-a-cycle
        return min(abs(a-b), d-abs(a-b))

    arr = [0] + arr
    # arr = arr[::-1]

    def remove_consecutive_duplicates(lst):
        res = []
        for x in lst:
            if res and x == res[-1]:
                continue
            res.append(x)
        return res

    arr = remove_consecutive_duplicates(arr)
    if len(arr) == 1:
        # because got zero
        return 0

    log(arr)

    n = len(arr)
    dp = defaultdict(lambda: LARGE)  # (l,r,target): cost  - r exclusive
    for i in range(n):
        dp[i,i+1,arr[i]] = 0


    for size in range(2,n+1):
        # log(dp)
        for left in range(n-size+1):
            right = left+size

            left_target = arr[left]
            right_target = arr[right-1]

            dp[left,right,left_target] = LARGE
            dp[left,right,right_target] = LARGE

            mincost = LARGE
            # log(left, right, left_target)

            for divider in [left+1]:
                moving_target = arr[divider]
                cost = dp[left, divider, left_target] + dp[divider, right, moving_target] + dist(left_target, moving_target)
                mincost = min(mincost, cost)

            for divider in [left+1]:
                moving_target = arr[right-1]
                cost = dp[left, divider, left_target] + dp[divider, right, moving_target] + dist(left_target, moving_target)
                mincost = min(mincost, cost)

            dp[left,right,left_target] = min(dp[left,right,left_target], mincost)

            mincost = LARGE
            # log(left, right, right_target)

            for divider in [right-1]:
                moving_target = arr[left]
                cost = dp[left, divider, moving_target] + dp[divider, right, right_target] + dist(right_target, moving_target)
                mincost = min(mincost, cost)

            for divider in [right-1]:
                moving_target = arr[divider-1]
                cost = dp[left, divider, moving_target] + dp[divider, right, right_target] + dist(right_target, moving_target)
                mincost = min(mincost, cost)
                
            dp[left,right,right_target] = min(dp[left,right,right_target], mincost)
            log(left,right, dp[left,right,left_target], dp[left,right,right_target])

    return dp[0,n,0]
    # def dp(l,r,target):
    #     for i in range(l,r):


    # return dp(0,d,0)

    # def dp()

    return arr.count(1)


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
    a,d = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(arr, d)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    # print(res)
