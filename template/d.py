#!/usr/bin/env python3
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

M9 = 10**9 + 7  # 998244353
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

# ---------------------------- template ends here ----------------------------


def solve_(srr, mrr):
    # your solution here
    psum = [0]
    pmin = [0]
    pmax = [0]
    # ssum = [0]
    smin = [0]
    smax = [0]

    curval = 0
    curmin = 0
    curmax = 0

    for x in srr:
        curval += x
        curmin = min(curmin, curval)
        curmax = max(curmax, curval)
        psum.append(curval)
        pmin.append(curmin)
        pmax.append(curmax)

    curval = 0
    curmin = 0
    curmax = 0

    for x in srr[::-1]:
        curval += -x
        curmin = min(curmin, curval)
        curmax = max(curmax, curval)
        # ssum.append(curval)
        smin.append(curmin)
        smax.append(curmax)
    
    # ssum = ssum[::-1]
    smin = smin[::-1]
    smax = smax[::-1]

    # log(psum)
    # log(pmin)
    # log(pmax)
    # log(ssum)
    # log(smin)
    # log(smax)

    res = []

    for a,b in mrr:
        # log()
        maxx = 0
        minn = 0
        end_point = psum[-1]-psum[b]+psum[a-1]
        maxx = max(0, pmax[a-1], end_point+smax[b])
        minn = min(0, pmin[a-1], end_point+smin[b])
        # log(end_point, smax[b], smin[b])
        # log(pmin[a-1], psum[-1], psum[b], psum[a-1], smin[b])
        # log(a,b,maxx,minn)
        # log()
        res.append(maxx-minn+1)

    # log()

    return res

cout = []
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
    _,k = list(map(int,input().split()))
    # lst = list(map(int,input().split()))
    srr = input().strip()
    srr = [1 if x == "+" else -1 for x in srr]

    # read multiple rows
    mrr = read_matrix(k)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str

    res = solve(srr, mrr)  # include input here
    
    # print result
    # Google and Facebook - case number required
    # print("Case #{}: {}".format(case_num+1, res))
    cout.extend(res)
    # Other platforms - no case number required
    # print(res)
    # print(len(res))
    # print(*res)  # print a list with elements
    # for r in res:  # print each list in a different line
        # print(res)
        # print(*res)
print("\n".join(str(r) for r in cout))