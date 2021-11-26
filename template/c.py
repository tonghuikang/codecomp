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



# Python3 approach to finding the XOR_SUM

# Returns sum of XORs of all subsets
def xorSum(arr):
    n = len(arr)

    bits = 0

    # Finding bitwise OR of all elements
    for i in range(n):
        bits |= arr[i]

    ans = bits * pow(2, n-1, M9)

    return ans

def solve_(n,mrr):
    # your solution here

    restriction = [[0 for _ in range(31)] for _ in range(n+1)]

    for l,r,k in mrr:
        l -= 1
        r -= 1
        srr = bin(k)[2:].zfill(31)[::-1]
        log(k, srr)
        for i,x in enumerate(srr):
            if x == "0":
                restriction[l][i] += 1
                restriction[r+1][i] -= 1

    log("restriction")
    log(restriction)

    rrr = [[1 for _ in range(31)] for _ in range(n)]

    for j in range(31):
        csum = 0
        for i in range(n):
            csum += restriction[i][j]
            if csum == 0:
                rrr[i][j] = 0

    log("rrr")
    log(rrr)

    res = [0 for _ in range(n)]
    for i,row in enumerate(rrr):
        val = sum(2**i * x for i,x in enumerate(row[:30]))
        res[i] = val

    log(res)

    return xorSum(res)


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    n,m = list(map(int,input().split()))
    # lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(m)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n,mrr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
