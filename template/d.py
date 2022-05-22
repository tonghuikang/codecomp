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

# https://leetcode.com/problems/count-different-palindromic-subsequences/discuss/109510/Python-DP%2BDFS-O(n2)-with-Explanations

# https://codeforces.com/blog/entry/56448

LARGE = 500
p = 10**9 + 7
factorial_mod_p = [1 for _ in range(LARGE)]
for i in range(1,LARGE):
    factorial_mod_p[i] = (factorial_mod_p[i-1]*i)%p


def ncr_mod_p(n, r, p=p):
    num = factorial_mod_p[n]
    dem = factorial_mod_p[r]*factorial_mod_p[n-r]
    return (num * pow(dem, p-2, p))%p


def solve_(srr):
    # your solution here
    n = len(srr)
    s = srr
    
    dp = [[[0 for _ in range(n+2)] for _ in range(n+2)] for _ in range(n+2)]
    for i in range(n,0,-1):
        for j in range(i,n+1):
            dp[i][j][0] = 1
            dp[i][j][1] = j-i+1
            if i+1 == j:
                if (s[i-1] == s[j-1]):
                    dp[i][j][2] = 1
                continue

            for k in range(2, n+1):
                dp[i][j][k] = ((s[i-1]==s[j-1])*dp[i+1][j-1][k-2]+dp[i][j-1][k]+dp[i+1][j][k]-dp[i+1][j-1][k])%p


    counts = [0]*(n+1)
    for k in range(1,n+1):
        counts[k] += dp[1][n][k]

    log(counts)

    factor = factorial_mod_p[401]
    res = factor

    for i,x in enumerate(counts[1:-1], start=1):
        space = ncr_mod_p(n, i)
        count = counts[i]
        # log(count, space)
        count = count*factor*pow(space, p-2, p)
        res += count

    res = res%p
    res = res*pow(factor, p-2, p)
    res = res%p
    
    return res


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    k = int(input())

    # read line as a string
    srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(srr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    # print(res)
