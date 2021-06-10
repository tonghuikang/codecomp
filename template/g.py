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


# max x+y
# st  xa + yb <= p
#     xb + ya <= q

def possible(p,q,a,b,x,y):
    if x < 0 or y < 0:
        return False
    # log(x*a + y*b, p, x*b + y*a, q)
    return x*a + y*b <= p and x*b + y*a <= q

def solve_(x,y,a,b):
    # your solution here
    if a == b:
        return min(x//a, y//a)

    p,q,a,b = x,y,a,b
    p,q = sorted([p,q])
    a,b = sorted([a,b])

    x = (a*q - b*p) / (a*a - b*b)
    y = (a*p - b*q) / (a*a - b*b)

    # log(x,y)
    if x <= 0 or y <= 0:
        return max(0, min(p//a, q//b), min(p//b, q//a))

    xx = int(x)
    yy = int(y)
    maxres = xx + yy
    assert possible(p,q,a,b,xx,yy) or possible(p,q,a,b,yy,xx)

    for i in list(range(1,2)) + [p,q,a,b,math.gcd(p,q),math.gcd(a,b),abs(a-b),abs(p-q)]:
        xx = int(x)+i
        yy = int((q-x*b)/a)
        # log(xx,yy)
        if possible(p,q,a,b,xx,yy) or possible(p,q,a,b,yy,xx):
            maxres = max(maxres, xx + yy)

        xx = int(x)+i
        yy = int((q-x*a)/b)
        # log(xx,yy)
        if possible(p,q,a,b,xx,yy) or possible(p,q,a,b,yy,xx):
            maxres = max(maxres, xx + yy)

        yy = int(y)+i
        xx = int((p-y*b)/a)
        # log(xx,yy)
        if possible(p,q,a,b,xx,yy) or possible(p,q,a,b,yy,xx):
            maxres = max(maxres, xx + yy)
    
        yy = int(y)+i
        xx = int((p-y*a)/b)
        # log(xx,yy)
        if possible(p,q,a,b,xx,yy) or possible(p,q,a,b,yy,xx):
            maxres = max(maxres, xx + yy)

    return maxres


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
    x,y,a,b = list(map(int,input().split()))
    # lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(x,y,a,b)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)