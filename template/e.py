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


def solve_(nrr, mrr, qrr):
    # your solution here
    # just need to track three points

    origin = 0,0
    x0 = 1,0
    y0 = 0,1

    orr = [origin]
    xrr = [x0]
    yrr = [y0]

    for lst in mrr:
        if lst[0] == 2:  # x,y -> -y,x
            origin = -origin[1], origin[0]
            x0 = -x0[1], x0[0]
            y0 = -y0[1], y0[0]
        elif lst[0] == 1:  # x,y -> y,-x
            origin = origin[1], -origin[0]
            x0 = x0[1], -x0[0]
            y0 = y0[1], -y0[0]
        elif lst[0] == 3:
            p = lst[1]
            origin = p+(p-origin[0]), origin[1]
            x0 = p+(p-x0[0]), x0[1]
            y0 = p+(p-y0[0]), y0[1]
        elif lst[0] == 4:
            p = lst[1]
            origin = origin[0], p+(p-origin[1])
            x0 = x0[0], p+(p-x0[1])
            y0 = y0[0], p+(p-y0[1])
        orr.append(origin)
        xrr.append(x0)
        yrr.append(y0)

    # log(orr)
    # log(xrr)
    # log(yrr)

    res = []
    for a,b in qrr:
        p,q = nrr[b-1]
        o = orr[a]
        x = xrr[a]
        y = yrr[a]

        u = o[0] + p*(x[0]-o[0]) + q*(y[0]-o[0])
        v = o[1] + p*(x[1]-o[1]) + q*(y[1]-o[1])
        res.append("{} {}".format(u,v))
        
    return res


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    # lst = list(map(int,input().split()))

    # read multiple rows
    n = int(input())
    nrr = read_matrix(n)  # and return as a list of list of int

    m = int(input())
    mrr = read_matrix(m)  # and return as a list of list of int

    q = int(input())
    qrr = read_matrix(q)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str

    res = solve(nrr, mrr, qrr)  # include input here
    
    # print result
    # Google and Facebook - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    # print(res)
    print("\n".join(res))
    # print(len(res))
    # print(*res)  # print a list with elements
    # for r in res:  # print each list in a different line
        # print(res)
        # print(*res)