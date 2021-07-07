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


eps = 10**(-11)

def solve_(a,b,c,v):
    # your solution here
    
    # simulations
    stack = [(a,b,c,1,1)]  # c,m,p,turn,prob
    res = 0.0
    while stack:
        # print(stack)
        a,b,c,t,p = stack.pop()

        # assert abs(a + b + c - 1) < 10**(-9)

        # draw c
        res += t*c*p

        if p < eps:
            continue

        # draw b
        if b >= v:
            if a > eps:
                stack.append([a + v/2, b-v, c + v/2, t+1, p*b])
            else:
                stack.append([0,       b-v, c + v,   t+1, p*b])

        else:
            if a > eps:
                stack.append([a + b/2, 0, c + b/2, t+1, p*b])
            else:
                stack.append([0,       0, c + b,   t+1, p*b])

        # draw a
        if a >= v:
            if b > eps:
                stack.append([a-v, b + v/2, c + v/2, t+1, p*a])
            else:
                stack.append([a-v, 0,       c + v,   t+1, p*a])

        else:
            if b > eps:                    
                stack.append([0, b + a/2, c + a/2, t+1, p*a])
            else:
                stack.append([0, 0,       c + a,   t+1, p*a])


    return res


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
    a,b,c,v = list(map(float,input().split()))
    # lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(a,b,c,v)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
    # break