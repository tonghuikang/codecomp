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


def solve_(srr,b,c):
    # your solution here

    srr = [int(x) for x in srr]

    if c%2 == 1:
        srr = [1-x for x in srr]

    if srr.count(0) == 0:
        srr[-1] = 1
        res = [0 for _ in srr]
        res[-1] = c
        return srr, res

    log(srr)

    allowance = c
    res = [0 for _ in srr]
    pairing = srr.count(0)
    for i in range(len(srr)):
        x = srr[i]
        if x==0 and allowance and not (pairing == 1 and allowance%2 == 0):
            res[i] += 1
            srr[i] += 1
            allowance -= 1
            pairing -= 1

    log(allowance, srr)

    assert allowance%2 == 0
    
    zeropos = []
    onepos = []
    for i,x in enumerate(srr):
        if x == 0:
            zeropos.append(i)
        if x == 1:
            onepos.append(i)

    for a,b in zip(zeropos, onepos[::-1]):
        if allowance >= 2 and b > a:
            log(a,b)
            allowance -= 2
            srr[a] += 1
            srr[b] -= 1
            res[a] += 1
            res[b] += 1

    log(srr)

    res[0] += allowance
    assert sum(res) == c

    return srr, res


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    b,c = list(map(int,input().split()))
    srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    srr, res = solve(srr,b,c)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    srr = "".join(str(x) for x in srr)
    res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required
    print(srr)
    print(res)
