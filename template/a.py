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


def solve_(a0,b0,c0):
    # your solution here

    # 3 + 3 + 4
    # 4 + 4 + 2
    # 4 + 2 + 2 + 2
    # 2 + 2 + 2 + 2 + 2

    a,b,c = a0,b0,c0

    def op334():
        nonlocal a,b,c
        set334 = min(b//2, c)
        c -= set334
        b -= set334*2
        return set334

    def op442():
        nonlocal a,b,c
        set442 = min(c//2, a)
        c -= set442*2
        a -= set442
        return set442

    def op4222():
        nonlocal a,b,c
        set4222 = min(c, a//3)
        c -= set4222
        a -= set4222*3
        return set4222

    def op22222():
        nonlocal a,b,c
        set22222 = a//5
        a -= set22222*5
        return set22222

    def op3322():
        nonlocal a,b,c
        set2233 = min(b//2, a//2)
        a -= set2233*2
        b -= set2233*2
        return set2233

    maxcnt = 0

    for perm in itertools.permutations([op334, op442, op4222, op22222, op3322]):
        a,b,c = a0,b0,c0

        cnt = 0
        for op in perm:
            cnt += op()
            # log(op.__name__, cnt)
        maxcnt = max(maxcnt, cnt)

    return maxcnt


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
    a,b,c = list(map(int,input().split()))
    # lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(a,b,c)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
