#!/usr/bin/env python3
import sys
import getpass  # not available on codechef
# import math, random
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

def check_mex_good(arr):
    if not arr:
        return False
    seen = set()
    for x in arr:
        seen.add(x)
        for i in range(10):
            if i not in seen:
                mex = i
                if abs(x-mex) > 1:
                    return False
                break
    return True

def solve_(arr):
    # your solution here

    if OFFLINE_TEST:
        ref = 0
        for comb in itertools.product([0,1], repeat=len(arr)):
            brr = [x for c,x in zip(comb,arr) if c]
            if check_mex_good(brr):
                ref += 1
        log(ref)

    dp_filled = defaultdict(int)
    dp_filled[-1] = 1

    dp_unfilled = defaultdict(int)

    res = 0

    for x in arr:
        inc = 0
        inc += dp_unfilled[x] + dp_filled[x-2]
        inc += dp_filled[x] + dp_filled[x-1]
        inc += dp_unfilled[x+2]
        res += inc

        dp_unfilled[x] = dp_unfilled[x]*2 + dp_filled[x-2]
        dp_filled[x] = dp_filled[x]*2 + dp_filled[x-1]

        # dp_filled[x+1] += dp_unfilled[x+1]

        # if x >= 2:
        #     dp_unfilled[x], dp_filled[x] = \
        #         dp_unfilled[x]*2 + dp_filled[x-2], \
        #         dp_filled[x]*2 + dp_filled[x-1]
        # else:
        #     dp_unfilled[x], dp_filled[x] = \
        #         dp_unfilled[x]*2 + dp_filled[x-2], \
        #         dp_filled[x]*2 + dp_filled[x-1] + dp_unfilled[x+1]

        log(inc)
        log({k:v for k,v in dp_unfilled.items() if v > 0})
        log({k:v for k,v in dp_filled.items() if v > 0})
        log()

    log(res)
    if OFFLINE_TEST:
        assert res == ref

    return res


if OFFLINE_TEST:
    if False:
        import random
        for _ in range(10000):
            solve([random.randint(0,5) for _ in range(random.randint(1,4))])


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

    res = solve(arr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
