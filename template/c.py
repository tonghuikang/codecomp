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

def findGCD(x, y, z, res):

    # Store the maximum GCD obtained
    # by either incrementing, decrementing
    # or not changing A[i]
    ans = math.gcd(x, res)
    ans = max(ans, math.gcd(y, res))
    ans = max(ans, math.gcd(z, res))

    # Return the maximum GCD
    return ans


def maximumGCD(A, K):
    N = len(A)

    # Initialize a dp table of size N*3
    dp = [[0 for x in range(3)]
             for y in range(N)]

    # Base Cases:
    # If only one element is present
    dp[0][0] = A[0]
    dp[0][1] = A[0] + K
    dp[0][2] = A[0] - K

    # Traverse the array A[] over
    # indices [1, N - 1]
    for i in range(1, N):

        # Store the previous state results
        x = dp[i - 1][0]
        y = dp[i - 1][1]
        z = dp[i - 1][2]

        # Store maximum GCD result
        # for each current state
        dp[i][0] = findGCD(x, y, z, A[i])
        dp[i][1] = findGCD(x, y, z, A[i] + K)
        dp[i][2] = findGCD(x, y, z, A[i] - K)

    # Store the required result
    mx = max([3, dp[N - 1][0],
                 dp[N - 1][1],
                 dp[N - 1][2]])

    # Return the result
    return mx


def binary_search(func_,       # condition function
                  first=True,  # else last
                  target=True, # else False
                  left=0, right=2**63-1) -> int:
    # https://leetcode.com/discuss/general-discussion/786126/
    # ASSUMES THAT THERE IS A TRANSITION
    # MAY HAVE ISSUES AT THE EXTREMES

    def func(val):
        # if first True or last False, assume search space is in form
        # [False, ..., False, True, ..., True]

        # if first False or last True, assume search space is in form
        # [True, ..., True, False, ..., False]
        # for this case, func will now be negated
        if first^target:
            return not func_(val)
        return func_(val)

    while left < right:
        mid = (left + right) // 2
        if func(mid):
            right = mid
        else:
            left = mid + 1
    if first:  # find first True
        return left
    else:      # find last False
        return left-1


def solve_(arr, k):
    res = 1
    if k <= 10**12:
        res = maximumGCD(arr, k)
    # binary search

    def func(val):
        # return true if can increase the array to get gcd of k
        return sum((-x)%val for x in arr) <= k

    res2 = binary_search(func, left=1, first=False, target=True)

    return max(res, res2)


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
    _,k = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(arr, k)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
