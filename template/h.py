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


def longest_increasing_subsequence(nums):
    res = []
    # leetcode.com/problems/longest-increasing-subsequence/discuss/667975/
    dp = [MAXINT] * (len(nums) + 1)
    for elem in nums:
        dp[bisect.bisect_left(dp, elem)] = elem
        res.append(dp.index(elem)+1)
    return res


def solve_(arr):
    # your solution here
    res1 = longest_increasing_subsequence(arr)
    res2 = longest_increasing_subsequence(arr[::-1])[::-1]

    maxres = max(max(res1), max(res2))

    log(res1)
    log(res2)

    for i,x in enumerate(res2):
        start = max(0, i-x)
        log(i, start)
        for j,y in enumerate(res1[:start]):
            log(i,start,x,j,y)
            if arr[j] > arr[i]:
                res = x+y
                log(res)
                maxres = max(maxres, res)

    # maxres = dp.index(MAXINT)

    # for i in range(len(arr)//2, len(arr)):
    #     dp1 = longest_increasing_subsequence(arr[:i])
    #     dp2 = longest_increasing_subsequence([-x for x in arr[i:][::-1]])
    #     res = dp1.index(MAXINT) + dp2.index(-arr[-1])
        # maxres = max(maxres, res)
    
    return maxres


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    maxres = 1
    res = solve(arr)  # include input here
    maxres = max(maxres, res)
    res = solve(arr[::-1])  # include input here
    maxres = max(maxres, res)

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)