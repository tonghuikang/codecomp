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

def verify(arr, k):
    log()
    log(arr, k)
    brr = [-1 for _ in arr]
    n = len(arr)
    assert max(arr) == n
    assert min(arr) == 1
    assert 0 <= k <= n

    last_lower = 0
    last_higher = n+1

    for i,x in enumerate(arr):
        if x <= k:
            brr[x-1] = last_higher
        if x > k:
            brr[x-1] = last_lower

        if x <= k:
            last_lower = x
        if x > k:
            last_higher = x

    return brr


log(verify([1,3,2,4], 2))
log(verify([1,2,3,4,5,6], 3))
log(verify([6,5,4,3,2,1], 3))

log(verify([1,2,3,4,5,6], 0))
log(verify([1,2,3,4,5,6], 1))
log(verify([1,2,3,4,5,6], 2))
log(verify([1,2,3,4,5,6], 3))
log(verify([1,2,3,4,5,6], 4))
log(verify([1,2,3,4,5,6], 5))
log(verify([1,2,3,4,5,6], 6))

log(verify([4,3,1,5,2,6], 4))
log(verify([4,3,1,5,2,6], 2))
log(verify([4,3,1,5,2,6,7], 2))
log(verify([4,3,1,5,2,6,7], 3))
log(verify([4,3,1,5,2,6,7], 4))


def solve_(arr, n):
    # your solution here

    
    # assert verify(brr, k) == arr
    # return brr
    pass


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    n = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(arr, n)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
